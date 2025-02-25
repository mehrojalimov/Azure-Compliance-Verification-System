from fastapi import FastAPI, Depends
from app.routes import client_routes, compliance_routes, auth

app = FastAPI(title="Automated Client Risk Assessment Tool")

# Include Routes
app.include_router(client_routes.router, prefix="/clients", tags=["Clients"])
app.include_router(compliance_routes.router, prefix="/compliance", tags=["Compliance"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def root():
    return {"message": "Welcome to the Automated Client Risk Assessment Tool"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
