from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    expires = datetime.utcnow() + timedelta(hours=1)
    to_encode = data.copy()
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, "SECRET_KEY", algorithm="HS256")
    return encoded_jwt

@app.post("/token")
def login(user_credentials: UserCredentials):
    user = authenticate_user(user_credentials)
    if user:
        token = create_access_token({"sub": user.username})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")
