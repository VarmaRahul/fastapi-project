from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app import database, config
from app.models.models import User

# This line tells FastAPI where the login endpoint is
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # 1. Decode the JWT
        payload = jwt.decode(token, config.settings.secret_key, algorithms=[config.settings.algorithm])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # 2. Fetch the user from the DB to ensure they still exist
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception

    return user