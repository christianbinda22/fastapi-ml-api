from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db, engine
from app.database.base import Base
from app.models import user, user_profile

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/health/db")
def db_health_check(db: Session = Depends(get_db)):
    return {"database": "connected"}