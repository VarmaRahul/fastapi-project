from passlib.context import CryptContext

from datetime import datetime, timedelta, timezone
from jose import jwt
from app.config import settings

# Tell Passlib to use bcrypt for hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    
    # 1. Use the new 3.12 compliant way to get UTC time
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    
    # 2. Add the expiration to the payload
    to_encode.update({"exp": expire})
    
    # 3. Create the JWT
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    
    return encoded_jwt