from sqlalchemy import create_engine,text
from langchain.tools import tool
import pandas as pd
from app.core.states import State
from langgraph.prebuilt import ToolNode
from app.core.LLM import ModelLoader
from datetime import datetime

llm=ModelLoader().model_loading()

engine = create_engine("postgresql+psycopg2://postgres:nithish@localhost:5432/Booking")
try:
    with engine.connect() as conn:
        print("connected to postgressql")
except Exception as e:
    print(e)

@tool
def booking_system(seat_no: int, passenger_name: str, source: str, destination: str, date_input:str):
    """Based on the user details, bus booking is processed here."""
    # detail = state["detail"][0]
    # seat_no = detail.get("seat_no", None)
    # passenger_name = detail.get("passenger_name", None)
    # source = detail.get("source",None)
    # destination = detail.get("destination", None)
    # date_input = detail.get("date_input", None)

    if seat_no <1:
        raise ValueError("the seat no greater than 1")
    
    if not all([passenger_name, source, destination, date_input]):
        raise ValueError("One or more required details are missing")

    result = ""
    query = f"SELECT * FROM booking WHERE seat_no = {seat_no}"
    df = pd.read_sql(query, con=engine)

    if df.empty:
        insert = f"""
        INSERT INTO booking(seat_no, passenger_name, source, destination, date_input)
        VALUES ({seat_no}, '{passenger_name}', '{source}', '{destination}', '{date_input}')
        """
        from sqlalchemy import text
        with engine.connect() as conn:
            result = conn.execute(text(insert))
            conn.commit()

        if result.rowcount > 0:
            return "Bus booking has been successfully completed"
        else:
            return "Booking failed. Please try another seat."
    else:
        return f"Seat number {seat_no} is already booked."


@tool
def remove_booking(seat_no:int):
    """detele a booking based on the seat number provided by the user."""
    # detail = seat_no

    if seat_no < 1:
        raise ValueError("Seat number is required to remove a booking.")

    # Check if the booking exists
    query = f"SELECT * FROM booking WHERE seat_no = {seat_no}"
    df = pd.read_sql(query, con=engine)

    if df.empty:
        return f"No booking found for seat number {seat_no}."

    # Perform deletion
    delete_query = f"DELETE FROM booking WHERE seat_no = {seat_no}"

    with engine.connect() as conn:
        result = conn.execute(text(delete_query))
        conn.commit()

    if result.rowcount > 0:
        return f"Booking for seat number {seat_no} has been successfully removed."
    else:
        return "Deletion failed. Please try again."

    
@tool
def updated_system(seat_no: int, passenger_name: str, source: str, destination: str, date_input:str):
    """Updates existing bus booking details based on the seat number."""
    # detail = state["detail"][0]
    # seat_no = detail.get("seat_no", None)
    # source = detail.get('source',None)
    # passenger_name = detail.get("passenger_name", None)
    # destination = detail.get("destination", None)
    # date_input = detail.get("date_input", None)
    
    if seat_no <1:
        raise ValueError("the seat no greater than 1")
    
    if not all([passenger_name, source, destination, date_input]):
        raise ValueError("One or more required details are missing")

    from sqlalchemy import text
    result = ""

    # Check if booking exists
    query = f"SELECT * FROM booking WHERE seat_no = {seat_no}"
    df = pd.read_sql(query, con=engine)

    if df.empty:
        return f"No booking found for seat number {seat_no}."

    # Prepare update fields
    update_fields = []
    if passenger_name:
        update_fields.append(f"passenger_name = '{passenger_name}'")
    if source:
        update_fields.append(f"source = '{source}'")
    if destination:
        update_fields.append(f"destination = '{destination}'")
    if date_input:
        update_fields.append(f"date_input = '{date_input}'")
    
    if not update_fields:
        return "No details provided to update."

    update_query = f"""
    UPDATE booking
    SET {', '.join(update_fields)}
    WHERE seat_no = {seat_no}
    """

    with engine.connect() as conn:
        result = conn.execute(text(update_query))
        conn.commit()

    if result.rowcount > 0:
        return f"Booking for seat number {seat_no} has been successfully updated."
    else:
        return "Update failed. Please try again."


@tool
def fetch_bus_booking_system(seat_no: int) -> dict:
    """
    Fetch the booking data from the database for a given seat number.
    """
    query = f"SELECT * FROM booking WHERE seat_no = {seat_no}"
    df = pd.read_sql(query, con=engine)

    if df.empty:
        return {"message": f"No passenger is booked for seat number {seat_no}."}
    else:
        # Assuming only one row per seat_no
        row = df.iloc[0].to_dict()
        return {"message": "Booking found", "data": row}
    
@tool
def fetch_all_data() -> dict:
    """Fetch all the booking records in the database."""
    query = "SELECT * FROM booking"
    df = pd.read_sql(query, con=engine)

    if df.empty:
        return {"message": "No passenger is booked right now"}
    else:
        # Convert DataFrame to list of dicts
        records = df.to_dict(orient="records")
        return {"message": f"Total {len(records)} bookings found", "data": records}




tools=[booking_system,fetch_bus_booking_system,remove_booking,updated_system,fetch_all_data]

tool_node=ToolNode(tools)

bind_tools=llm.bind_tools(tools=tools)