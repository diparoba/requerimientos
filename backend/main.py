from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, database, schemas

app = FastAPI(title="PhysioCare API")

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to PhysioCare API"}

@app.get("/exercises", response_model=List[schemas.Exercise])
def get_exercises(db: Session = Depends(get_db)):
    return db.query(models.Exercise).all()

@app.post("/chat/send")
def send_message(message: str):
    # Place holder for chat logic
    return {"status": "Message sent", "message": message}
