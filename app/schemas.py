from pydantic import BaseModel

class TokenData(BaseModel):
    username: str | None = None

class UserCreate(BaseModel):
    username: str
    password: str

class OAuthClientCreate(BaseModel):
    client_id: str
    client_secret: str
    redirect_uri: str
