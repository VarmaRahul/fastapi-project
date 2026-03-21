from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.database import engine, Base
from app.router import users, auth, orders, index
from app.database import get_db
import logging
from contextlib import asynccontextmanager

# This line creates the tables in Postgres if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="GitOps Platform API")

# 1. Setup Structured Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 2. Define the Lifespan (Startup & Shutdown)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup Logic ---
    logger.info("🚀 Ultimate Platform API is starting up...")
    logger.info("Connecting to PostgreSQL...")
    
    yield  # This is where the app runs
    
    # --- Shutdown Logic ---
    logger.info("🛑 Ultimate Platform API is shutting down...")
    logger.info("Closing database connections...")

# 3. Pass lifespan to the FastAPI instance
app = FastAPI(lifespan=lifespan)

# 4. Your Health & Ready Checks
@app.get("/health", tags=['Observability'])
def health_check():
    return {"status": "healthy"}

@app.get("/ready", tags=['Observability'])
def ready_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ready"}
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise HTTPException(status_code=503, detail="Database not reachable")

# Include Routers
app.include_router(index.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(orders.router)
