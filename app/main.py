from fastapi import FastAPI
from app.router import users, orders

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