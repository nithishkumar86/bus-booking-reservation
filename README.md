The Bus Reservation System is an AI-powered application that allows users to book, update, delete, and fetch bus reservations seamlessly. It integrates:

FastAPI backend (for booking APIs)
LangGraph + LLM Agent (Groq/OpenAI) (for natural language query understanding)
PostgreSQL for data storage
Streamlit UI (optional frontend for interaction)
Users can interact in plain English like:
“Book a seat for Nithish from Chennai to Bangalore on 2025-12-12 at 09:00 AM”
“Update my seat 3 to travel from Delhi to Mumbai on 2025-12-20 at 6:00 PM”
“Delete seat 1 from reservation”
“Fetch all my bookings”

The system will intelligently route the query to the right backend function (booking_system, update_booking, delete_booking, fetch_all_bookings).

Features

Natural language booking (LLM-powered)
CRUD operations: Create, Update, Delete, Fetch bookings Seat & schedule validation
Modular design using LangGraph for orchestration
Logging & monitoring built-in
Memory for multi-turn conversations

Clone Repository
git clone https://github.com/yourusername/bus-reservation-system.git
cd bus-reservation-system

Create Virtual Environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate   

Install Dependencies
pip install -r requirements.txt

Configure API Keys
Create a .env file with your credentials:

GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key 

To Run the Project
python main.py 

Tech Stack

Python 3.10+
FastAPI – REST backend
PostgreSQL - for datastorage
LangGraph – workflow orchestration
Groq LLM API – query understanding
Pydantic – data validation
Streamlit – frontend (optional)
Docker – containerization support
git - source code Management
Jenkins - Monitoring