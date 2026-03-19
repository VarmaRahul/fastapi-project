from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import database, oauth2
from app.models import models, schemas
from typing import List

router = APIRouter(prefix="/orders", tags=['Orders'])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, 
                 db: Session = Depends(database.get_db), 
                 current_user: models.User = Depends(oauth2.get_current_user)):
    
    # We automatically take the ID from the JWT token (current_user)
    new_order = models.Order(owner_id=current_user.id, **order.model_dump())
    
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.OrderResponse])
def get_my_orders(db: Session = Depends(database.get_db), 
                  current_user: models.User = Depends(oauth2.get_current_user)):
    
    # We only query orders where the owner_id matches the logged-in user
    orders = db.query(models.Order).filter(models.Order.owner_id == current_user.id).all()

    return orders

@router.get("/{id}", response_model=schemas.OrderResponse)
def get_order(id: int, 
              db: Session = Depends(database.get_db), 
              current_user: models.User = Depends(oauth2.get_current_user)):
    
    order = db.query(models.Order).filter(models.Order.id == id).first()
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
        
    # Security Check: Is this YOUR order?
    if order.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this order")
        
    return order
