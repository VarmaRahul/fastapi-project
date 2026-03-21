from fastapi import APIRouter

router = APIRouter(tags=["home"])

@router.get("/")
def get_index():
    return {"status": "This is the Home page"}