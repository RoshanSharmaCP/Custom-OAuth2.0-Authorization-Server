from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, utils, database
from app.schemas import UserCreate, OAuthClientCreate
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not utils.verify_password(password, user.hashed_password):
        return False
    return user

def create_user(db: Session, user: UserCreate):
    hashed_password = utils.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_oauth_client(db: Session, client: OAuthClientCreate):
    db_client = models.OAuthClient(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def generate_token(user: models.User):
    access_token = utils.create_access_token(data={"sub": user.username})
    return access_token
