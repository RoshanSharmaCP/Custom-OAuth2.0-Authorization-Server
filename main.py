from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
from auth import create_oauth_client,create_user, authenticate_user, generate_token
import database
from schemas import UserCreate, OAuthClientCreate
from fastapi.security import OAuth2PasswordRequestForm


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(database.get_db)):
    return create_user(db, user)

@app.post("/register_client", response_model=OAuthClientCreate)
def register_client(client: OAuthClientCreate, db: Session = Depends(database.get_db)):
    return create_oauth_client(db, client)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = generate_token(user)
    return {"access_token": access_token, "token_type": "bearer"}
