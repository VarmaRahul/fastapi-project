from fastapi import APIRouter

router = APIRouter(tags=["home"])

@router.get("/")
def health_check():
    return {"status": "This is the Home page"}