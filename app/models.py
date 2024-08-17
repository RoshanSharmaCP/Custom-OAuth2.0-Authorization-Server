from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class OAuthClient(Base):
    __tablename__ = "oauth_clients"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(String, unique=True, index=True)
    client_secret = Column(String)
    redirect_uri = Column(String)

class OAuthAuthorizationCode(Base):
    __tablename__ = "oauth_authorization_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    client_id = Column(Integer, ForeignKey('oauth_clients.id'))

    user = relationship("User")
    client = relationship("OAuthClient")
