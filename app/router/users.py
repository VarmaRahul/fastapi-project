from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models, schemas
from app.utils import hash_password
from app.oauth2 import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/health")
def health_check():
    return {"status": "user is healthy"}

@router.get("/me", response_model=schemas.UserResponse)
def get_my_profile(current_user: models.User = Depends(get_current_user)):
    # This function will NOT run if the token is invalid or missing
    # FastAPI handles the 401 Unauthorized error automatically!
    return current_user

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists (SRE Error Handling)
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pwd = hash_password(user.password) #Hash the password

    # Create the Model instance
    new_user = models.User(
        username=user.username, 
        email=user.email,
        password=hashed_pwd #Save the hash, NOT the plain text
    )

    # The Execution (The "Tap")
    db.add(new_user)     # Stage it
    db.commit()          # Save it to disk
    db.refresh(new_user) # Get the generated ID back

    return new_user