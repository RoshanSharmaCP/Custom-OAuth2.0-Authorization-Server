from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
# from . import models, schemas, crud, auth
from typing import List
from app.database import get_db
from app.database import Base
from app.models import Client, User
from app.schemas import UserCreate, ClientCreate, TokenRequest
from app.crud import create_user, create_client, create_authorization_code, get_authorization_code, update_access_token, invalidate_authorization_code
from app.auth import create_access_token, verify_access_token


Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.post("/user_registration", response_model=UserCreate)
def user_registration(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    return db_user

@app.post("/client_registration", response_model=ClientCreate)
def client_registration(client: ClientCreate, db: Session = Depends(get_db)):
    db_client = create_client(db, client)
    return db_client

@app.post("/authorize")
def authorize(user_id: int, client_secret: str, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.client_secret == client_secret).first()
    if not client:
        raise HTTPException(status_code=400, detail="Invalid client secret")

    auth_code = create_authorization_code(db, user_id, client.id, client.client_secret)
    return {"authorization_code": auth_code.authorization_code}

@app.post("/get_access_token")
def get_access_token(request: TokenRequest, db: Session = Depends(get_db)):
    auth_code = get_authorization_code(db, request.authorization_code)
    if not auth_code or auth_code.client_secret != request.client_secret:
        raise HTTPException(status_code=400, detail="Invalid authorization code or client secret")

    access_token = create_access_token(data={"user_id": auth_code.user_id})
    update_access_token(db, request.authorization_code, access_token)
    invalidate_authorization_code(db, request.authorization_code)
    
    return {"access_token": access_token}

@app.get("/access_resource")
def access_resource(access_token: str, db: Session = Depends(get_db)):
    payload = verify_access_token(access_token)
    user_id = payload.get("user_id")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": user.username}
