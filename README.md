# Automated Client Risk Assessment Tool

A **Costumer Due Diligence (CDD) solution** built with **FastAPI** and **Azure**, designed to streamline client risk assessment, automate document processing, and ensure regulatory compliance.

## 📌 Features
✔️ **Client Risk Profiling** – Assigns risk scores based on financial & background data.  
✔️ **KYC Document Upload** – Securely stores client verification documents on **Azure Blob Storage**.  
✔️ **Automated Compliance Checks** – Evaluates risk using **machine learning** and predefined rules.  
✔️ **User Authentication** – Secure login for compliance officers using **bcrypt** encryption.  
✔️ **Email Notifications** – Sends updates about risk evaluations & compliance status.  

---

## 🚀 Tech Stack
- **Backend:** FastAPI, SQLAlchemy, Uvicorn  
- **Database:** Azure SQL, PostgreSQL  
- **Cloud Services:** Azure Blob Storage, Azure App Service  
- **Frontend:** HTML, JavaScript, CSS  
- **Containerization:** Docker, Azure Container Registry  
- **Authentication:** JWT, Bcrypt 

## ⚙️ Installation
# Set Up Virtual Environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install Dependencies
pip install -r requirements.txt

# Set Up Environment Variables
Create a .env file with the following:

DATABASE_URL=postgresql://username:password@azure-host/db_name  
AZURE_STORAGE_CONNECTION_STRING="your-azure-blob-connection-string"  
EMAIL_HOST="smtp.your-email.com"  
EMAIL_USER="your-email@example.com"  
EMAIL_PASS="your-secure-password"  
SECRET_KEY="your-secret-key" 

# Run the Application
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
