from fastapi import FastAPI
from app.router import users, orders
from app.database import engine, Base

# This line creates the tables in Postgres if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="GitOps Platform API")

# SRE Health Checks
@app.get("/health", tags=["Monitoring"])
def health_check():
    return {"status": "healthy"}

@app.get("/ready", tags=["Monitoring"])
def readiness_check():
    # In Week 2, we will add a real DB check here
    return {"status": "ready"}

# Include Routers
app.include_router(users.router)
app.include_router(orders.router)