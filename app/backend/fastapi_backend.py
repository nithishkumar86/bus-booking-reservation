from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, StrictStr, StrictInt, field_validator
from datetime import datetime
from app.backend.schemas import CreateBody,UpdateBody,ResponseModel
from app.common.logger import get_logger
from app.core.Graph import GraphBuilder
from app.common.custom_exception import BookingException
from typing import Any,List
import json
import ast

logger = get_logger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------- Routes -----------
@app.post("/create", response_model=ResponseModel)
def create_booking(request: CreateBody):
    question = (
        f"My name is {request.passenger_name} and I want to book seat no {request.seat_no} "
        f"to travel from {request.source} to {request.destination} "
        f"on {request.date_input}."
    )
    logger.info(f"create booking question is created succesfully {question}")
    try:
        # Load the graph
        graph = GraphBuilder().graph_retrieval()
        config = {"configurable": {"thread_id": "1","recursion_limit": 100 }}
        response = graph.invoke({"messages": question},config = config,stream_mode='values')
        logger.info(f"create booking response {response} is created succesfully ")
        messages = response.get("messages", [])
        result = messages[-1].content if messages else "No response generated."
        return JSONResponse(status_code=200, content={"messages": result})
    except BookingException as e:
        logger.error(f"there is an error in create booking {str(e)}")
        raise HTTPException(status_code=404,detail=f"the error is {str(e)}")



@app.get("/retrieve/{seat_no}", response_model=ResponseModel)
def retrieve_booking(seat_no: int):
    if seat_no < 1:
        raise HTTPException(status_code=400, detail="Invalid seat number")
    
    question =f"Retrieve seat no {seat_no}"
    logger.info(f"retrieve booking question is created succesfully {question}")
    try:
        # Load the graph
        graph = GraphBuilder().graph_retrieval()
        config = {"configurable": {"thread_id": "1","recursion_limit": 100 }}
        response = graph.invoke({"messages": question},config=config,stream_mode='values')
        logger.info(f"booking is created : {response}  ")
        messages = response.get("messages", [])
        result = messages[-1].content if messages else "No response generated."
        return JSONResponse(status_code=200, content={"messages": result})
    except BookingException as e:
        logger.error(f"there is an error in retrieve booking {str(e)}")
        raise HTTPException(status_code=404,detail=f"the error is {str(e)}")

@app.put("/update", response_model=ResponseModel)
def update_booking(request: UpdateBody):
    question = (
        f"My name is {request.passenger_name} and I want to update seat no {request.seat_no} "
        f"to travel from {request.source} to {request.destination} "
        f"on {request.date_input}."
    )
    logger.info(f"update booking question is created succesfully {question}")
    try:
        # Load the graph
        graph = GraphBuilder().graph_retrieval()
        config = {"configurable": {"thread_id": "1","recursion_limit": 100 }}
        response = graph.invoke({"messages": question},config=config,stream_mode='values')
        messages = response.get("messages", [])
        result = messages[-1].content if messages else "No response generated."
        return JSONResponse(status_code=200, content={"messages": result})
    except BookingException as e:
        logger.error(f"there is an error in update booking {str(e)}")
        raise HTTPException(status_code=404,detail=f"the error is {str(e)}")


@app.delete("/delete/{seat_no}", response_model=ResponseModel)
def delete_booking(seat_no: int):
    if seat_no < 1:
        raise HTTPException(status_code=400, detail="Invalid seat number")
    question = f"Delete seat no {seat_no}"
    logger.info(f"delete booking question is created succesfully {question}")
    try:
        # Load the graph
        graph = GraphBuilder().graph_retrieval()
        config = {"configurable": {"thread_id": "1","recursion_limit": 100 }}
        response = graph.invoke({"messages": question},config=config,stream_mode='values')
        logger.info(f" delete successfull : {response} ")
        messages = response.get("messages", [])
        result = messages[-1].content if messages else "No response generated."
        return JSONResponse(status_code=200, content={"messages": result})
    except BookingException as e:
        logger.error(f"there is an error in delete booking {str(e)}")
        raise HTTPException(status_code=404,detail=f"the error is {str(e)}")
    

@app.get("/check", response_model=List[CreateBody])
def booked_list():
    question = f"fetch all the records in the database"
    logger.info(f"fetch booking question is created succesfully {question}")
    try:
        # Load the graph
        graph = GraphBuilder().graph_retrieval()
        config = {"configurable": {"thread_id": "1","recursion_limit": 100 }}
        response = graph.invoke({"messages": question},config=config,stream_mode='values')
        logger.info(f" fetch record successfull : {response} ")
        messages = response.get("messages", [])
        result = messages[-1].content if messages else "No response generated."
        if isinstance(result, str):
            try:
                result = json.loads(result)  # works if JSON string
            except:
                result = ast.literal_eval(result)  # works if Python dict string

        return JSONResponse(status_code=200, content=result)  # ✅ send real dict
    except BookingException as e:
        logger.error(f"there is an error in delete booking {str(e)}")
        raise HTTPException(status_code=404,detail=f"the error is {str(e)}")


    
