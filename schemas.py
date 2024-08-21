from pydantic import BaseModel

class TokenData(BaseModel):
    username: str | None = None

class UserCreate(BaseModel):
    username: str
    password: str

class OAuthClientCreate(BaseModel):
    redirect_uri: str
