from sqlalchemy.orm import Session
from uuid import uuid4
from app.models import User, Client, AuthorizationCode
from app.schemas import UserCreate, ClientCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_client(db: Session, client: ClientCreate):
    db_client = Client(redirect_uri=client.redirect_uri)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def create_authorization_code(db: Session, user_id: int, client_id: int, client_secret: str):
    authorization_code = str(uuid4())
    db_code = AuthorizationCode(user_id=user_id, client_id=client_id, client_secret=client_secret, authorization_code=authorization_code)
    db.add(db_code)
    db.commit()
    db.refresh(db_code)
    return db_code

def get_authorization_code(db: Session, authorization_code: str):
    authorization_code = db.query(AuthorizationCode).filter(AuthorizationCode.authorization_code == authorization_code).first()
    if not authorization_code:
        return None
    return authorization_code

def update_access_token(db: Session, authorization_code: str, access_token: str):
    db_code = db.query(AuthorizationCode).filter(AuthorizationCode.authorization_code == authorization_code).first()
    if db_code:
        db_code.access_token = access_token
        db.commit()
        db.refresh(db_code)
    return db_code

def invalidate_authorization_code(db: Session, authorization_code: str):
    db.query(AuthorizationCode).filter(AuthorizationCode.authorization_code == authorization_code).delete()
    db.commit()
