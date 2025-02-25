from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.routes.client_routes import clients

router = APIRouter()

@router.get("/check/{client_id}")
def check_compliance(client_id: int, db: Session = Depends(get_db)):
    client = next((c for c in clients if c["id"] == client_id), None)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    compliance_status = "Approved" if client["risk_score"] < 50 else "Needs Review"
    
    return {"client": client["name"], "risk_score": client["risk_score"], "status": compliance_status}
