from pydantic import BaseModel
from typing import List


class UserCreate(BaseModel):
    username: str
    password: str

class ClientCreate(BaseModel):
    redirect_uri: str

class TokenRequest(BaseModel):
    client_secret: str
    authorization_code: str

class ResourceRequest(BaseModel):
    access_token: str
