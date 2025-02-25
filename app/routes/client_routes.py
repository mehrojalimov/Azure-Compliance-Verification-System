from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.models.user import User
from app.models.risk_model import RiskModel

router = APIRouter()

clients = []  # Temporary in-memory storage (Replace with DB in production)

@router.post("/register")
def register_client(name: str, risk_indicators: list, db: Session = Depends(get_db)):
    risk_score = RiskModel.assess_risk({"risk_indicators": risk_indicators})
    new_client = {"id": len(clients) + 1, "name": name, "risk_score": risk_score}
    clients.append(new_client)
    
    return {"message": "Client registered successfully", "client": new_client}

@router.get("/{client_id}")
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = next((c for c in clients if c["id"] == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    return client
