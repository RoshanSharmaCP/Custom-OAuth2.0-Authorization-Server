from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, auth, database, schemas
from fastapi.security import OAuth2PasswordRequestForm


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/register", response_model=schemas.UserCreate)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return auth.create_user(db, user)

@app.post("/register_client", response_model=schemas.OAuthClientCreate)
def register_client(client: schemas.OAuthClientCreate, db: Session = Depends(database.get_db)):
    return auth.create_oauth_client(db, client)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.generate_token(user)
    return {"access_token": access_token, "token_type": "bearer"}
