import streamlit as st
import requests
from datetime import datetime
from app.common.logger import get_logger
import pandas as pd

st.set_page_config(page_icon="🛢", page_title="Bus Booking System", layout="centered")
st.header("🛢 Bus Booking System using Postgresql")

district = [
    'Ariyalur','Chengalpattu','Chennai','Coimbatore','Cuddalore','Dharmapuri','Dindigul','Erode',
    'Kallakkurichi','Kanchipuram','Kanniyakumari','Karur','Krishnagiri','Madurai','Mayiladuthurai',
    'Nagapattinam','Namakkal','Nilgiris','Perambalur','Pudukkottai','Ramanathapuram','Ranipet',
    'Salem','Sivaganga','Tenkasi','Thanjavur','Theni','Thoothukudi (Tuticorin)','Tiruchirappalli',
    'Tirunelveli','Tirupattur','Tiruppur','Tiruvallur','Tiruvannamalai','Tiruvarur','Vellore',
    'Viluppuram','Virudhunagar'
]

logger = get_logger(__name__)

# --- Date-time validation
def validate_datetime(dt_str: str) -> bool:
    try:
        datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False

# --- Create Booking
def create_method():
    seat_no = st.number_input("Enter the seat no", min_value=1, max_value=30, step=1)
    passenger_name = st.text_input("Enter your name")
    source = st.selectbox(label="Select your source", options=district)
    destination = st.selectbox(label="Select your destination", options=district)
    date_input = st.text_input("Enter date & time (Format: YYYY-MM-DD HH:MM:SS)")

    if st.button("Click to Process"):
        if seat_no < 1:
            st.warning("Seat number must be at least 1")
            return
        if not all([passenger_name, source, destination, date_input]):
            st.warning("There is some field missing, please select all")
            return
        if not validate_datetime(date_input):
            st.warning("Invalid date & time format. Please use YYYY-MM-DD HH:MM:SS")
            return

        payload = {
            "seat_no": seat_no,
            "passenger_name": passenger_name,
            "source": source,
            "destination": destination,
            "date_input": date_input
        }

        try:
            response = requests.post(url="http://127.0.0.1:8000/create", json=payload)
            if response.status_code == 200:
                message = response.json().get("messages", "")
                logger.info(f"new booking is created on this seat_no {seat_no} successfully")
                st.success(message)
            else:
                logger.error(f"error occured in create : {str(response.status_code)}")
                st.error(f"Failed! Status: {response.status_code}")
        except Exception as e:
            logger.error(f"an error occured  : {str(e)}")
            st.error(f"An error occurred: {str(e)}")

# --- Retrieve Booking
def retrieve_method():
    seat_no = st.number_input("Enter the seat no", min_value=1, max_value=30, step=1)

    if st.button("Click to Process"):
        if seat_no < 1:
            st.warning("Seat number must be at least 1")
            return
        payload = {"seat_no": seat_no}
        try:
            response = requests.get(url=f"http://127.0.0.1:8000/retrieve/{seat_no}")
            if response.status_code == 200:
                message = response.json().get("messages", "")
                logger.info(f"seat no {seat_no} is retrieved successfully")
                st.info(message)
            else:
                logger.error(f"error occured in retrieve: {str(response.status_code)}")
                st.error(f"Not found! Status: {response.status_code}")
        except Exception as e:
            logger.error(f"an error occured  : {str(e)}")
            st.error(f"An error occurred: {str(e)}")

# --- Update Booking
def update_method():
    seat_no = st.number_input("Enter the seat no", min_value=1, max_value=30, step=1)
    passenger_name = st.text_input("Enter your name")
    source = st.selectbox(label="Select your source", options=district)
    destination = st.selectbox(label="Select your destination", options=district)
    date_input = st.text_input("Enter date & time (Format: YYYY-MM-DD HH:MM:SS)")

    if st.button("Click to Process"):
        if seat_no < 1:
            st.warning("Seat number must be at least 1")
            return
        if not all([passenger_name, source, destination, date_input]):
            st.warning("There is some field missing, please select all")
            return
        if not validate_datetime(date_input):
            st.warning("Invalid date & time format. Please use YYYY-MM-DD HH:MM:SS")
            return

        payload = {
            "seat_no": seat_no,
            "passenger_name": passenger_name,
            "source": source,
            "destination": destination,
            "date_input": date_input
        }

        try:
            response = requests.put(url="http://127.0.0.1:8000/update", json=payload)
            if response.status_code == 200:
                message = response.json().get("messages", "")
                logger.info("data is updated successfully")
                st.success(message)
            else:
                logger.error(f"error occured in update : {str(response.status_code)}")
                st.error(f"Failed! Status: {response.status_code}")
        except Exception as e:
            logger.error(f"an error occured  : {str(e)}")
            st.error(f"An error occurred: {str(e)}")

# --- Delete Booking
def delete_method():
    seat_no = st.number_input("Enter the seat no to delete", min_value=1, max_value=30, step=1)

    if st.button("Click to Process"):
        if seat_no < 1:
            st.warning("Seat number must be at least 1")
            return
        payload = {"seat_no": seat_no}
        try:
            response = requests.delete(url=f"http://127.0.0.1:8000/delete/{seat_no}")
            if response.status_code == 200:
                message = response.json().get("messages", "")
                logger.info(f"seat no {seat_no} is deleted successfully")
                st.success(message)
            else:
                logger.error(f"error occured in delete {str(response.status_code)}")
                st.error(f"Delete failed! Status: {response.status_code}")
        except Exception as e:
            logger.error(f"an error occured  : {str(e)}")
            st.error(f"An error occurred: {str(e)}")
        

def booked_list():
    if st.button("Click to Process"):
        try:
            response = requests.get("http://127.0.0.1:8000/check")

            if response.status_code == 200:
                try:
                    result = response.json().get('messages', {})  # ✅ valid JSON
                    st.success("Bookings fetched successfully ✅")
                    st.success(result)  # pretty-print dict/list
                except ValueError:
                    st.error("Server did not return valid JSON")
            else:
                st.error(f"Error: {response.status_code}")
                logger.error(f"Check request failed: {response.text}")

        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            st.error(f"An error occurred: {str(e)}")





mode = st.selectbox("Choose an action", ["Select...", "book", "retrieve", "update", "delete", "booked_list"], index=0)

if mode == "book":
    st.subheader("📝 Book a Seat")
    create_method()
elif mode == "retrieve":
    st.subheader("🔍 Retrieve Booking")
    retrieve_method()
elif mode == "update":
    st.subheader("✏️ Update Booking")
    update_method()
elif mode == "delete":
    st.subheader("❌ Delete Booking")
    delete_method()
elif mode == "booked_list":
    st.subheader("get all booked_list")
    booked_list()

