# 🚌 Bus Booking System  

An AI-assisted **Bus Booking System** that supports **basic CRUD operations** with PostgreSQL and integrates **Groq API** for intelligent assistance.  
The project leverages **LangGraph for state management**, **FastAPI + Streamlit** for APIs & UI, and includes production-ready **logging and custom exception handling**.  
Deployment is handled with **Docker, Jenkins CI/CD, AWS ECR, and AWS Runner**.  

---

## 🔹 Overview  

- **CRUD Operations** → Manage bus routes, bookings, passengers using PostgreSQL.  
- **Groq API** → AI-enhanced user experience (e.g., query assistance, booking recommendations).  
- **LangGraph** → Workflow/state orchestration for chatbot-like booking flow.  
- **FastAPI** → Backend APIs for booking operations.  
- **Streamlit** → Interactive UI for booking system.  
- **Logging & Custom Exceptions** → Robust error handling and monitoring.  
- **CI/CD** → Automated deployment with Docker + Jenkins pipeline.  
- **AWS ECR + Runner** → Cloud-based container hosting and scaling.  

---

## ⚙️ Tech Stack  

- **Languages/Frameworks:** Python, FastAPI, Streamlit  
- **Database:** PostgreSQL  
- **AI/Orchestration:** Groq API, LangGraph  
- **DevOps Tools:** Docker, Jenkins, AWS ECR, AWS Runner  
- **Utilities:** Git, Logging, Custom Exception Handling  

---

## 🚀 Usage  

### 1️⃣ Local Development  

**Clone the repository**  
```bash
git clone https://github.com/nithishkumar86/bus-booking-reservation.git
cd app
```

**Create virtual environment & install dependencies**  
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

**Run FastAPI backend and streamlit Frontent By Running the Command in the Terminal**
```bash
python main.py
```


### 3️⃣ Deployment (CI/CD)  

#### Jenkins Pipeline  
- Pulls repo from GitHub.  
- Runs tests & lint checks.  
- Builds Docker image.  
- Pushes image to AWS ECR.  
- Deploys to AWS Runner.  

#### AWS ECR Push Example  
```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com
docker build -t bus-booking .
docker tag bus-booking:latest <account_id>.dkr.ecr.<region>.amazonaws.com/bus-booking:latest
docker push <account_id>.dkr.ecr.<region>.amazonaws.com/bus-booking:latest
```

---

## 📊 Logging & Error Handling  

- Centralized logging for API requests and booking operations.  
- Custom exception classes for database, validation, and booking errors.  
- Logs can be streamed to AWS CloudWatch for monitoring.  

---

## 📌 Features  

- ✅ Add, update, delete, and view bus bookings (CRUD)  
- ✅ PostgreSQL-backed persistence  
- ✅ AI-powered booking assistant (Groq API + LangGraph)  
- ✅ REST APIs (FastAPI) + UI (Streamlit)  
- ✅ Dockerized for portability  
- ✅ CI/CD with Jenkins + AWS Runner  
- ✅ Logging & production-ready error handling  

---



**Response**  
```json
{
  "booking_id": 101,
  "status": "confirmed"
}
```

---
