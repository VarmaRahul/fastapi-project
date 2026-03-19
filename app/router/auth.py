from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm # Add this import
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models
from app.utils import verify_password, create_access_token

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(db: Session = Depends(get_db), user_credentials: OAuth2PasswordRequestForm = Depends()):
    # 1. OAuth2PasswordRequestForm puts the email in 'username'
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    # 2. Verify password
    if not verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    # 3. Create Token
    access_token = create_access_token(data={"user_id": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}