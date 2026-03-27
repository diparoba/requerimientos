from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, database, schemas
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os


app = FastAPI(title="PhysioCare API")

# Serve static files for exercises
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/exercises", StaticFiles(directory=os.path.join(os.path.dirname(BASE_DIR), "frontend", "exercises")), name="exercises")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



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

@app.get("/treatments", response_model=List[schemas.Treatment])
def get_treatments(db: Session = Depends(get_db)):
    return db.query(models.Treatment).all()

@app.post("/chat/send")
def send_message(message: str):
    msg = message.lower()
    if "dolor" in msg or "duele" in msg:
        reply = "Siento mucho que tengas dolor. ¿Podrías indicarme del 1 al 10 qué tan intenso es en este momento?"
    elif "ejercicio" in msg or "rutina" in msg:
        reply = "Tengo varias rutinas preparadas para ti. ¿En qué zona del cuerpo te gustaría enfocarte hoy?"
    elif "lumbar" in msg or "espalda" in msg:
        reply = "Para la zona lumbar, te recomiendo el 'Estiramiento Lumbar' que ves en la sección de ejercicios. ¿Quieres que te explique cómo hacerlo?"
    else:
        reply = "Entiendo. Estoy aquí para ayudarte con tu rehabilitación. ¿Tienes alguna duda específica sobre tus ejercicios?"
    
    return {"status": "Message sent", "reply": reply}

