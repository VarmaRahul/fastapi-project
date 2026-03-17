from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# The URL format: postgresql://user:password@host:port/dbname
# Since your DB is on the same machine (via Docker), host is 'localhost'
SQLALCHEMY_DATABASE_URL = "postgresql://rahul_admin:password123@localhost:5432/ultimate_platform"

# The Engine is the starting point for any SQLAlchemy app
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Each instance of the SessionLocal class will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our database models to inherit from
Base = declarative_base()

# Dependency to get a DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()