from fastapi import FastAPI
from database import Base, engine
from models import User, Campaign, Battle, Combatant

# Create all database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Initiative Tracker")

@app.get("/")
def root():
    return {"message": "Initiative Tracker running!"}