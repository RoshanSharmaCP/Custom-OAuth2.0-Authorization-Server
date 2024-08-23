from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from uuid import uuid4
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_secret = Column(String, unique=True, index=True, default=lambda: str(uuid4()))
    redirect_uri = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class AuthorizationCode(Base):
    __tablename__ = "authorization_codes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))
    client_secret = Column(String)
    authorization_code = Column(String, unique=True)
    access_token = Column(String, nullable=True)
