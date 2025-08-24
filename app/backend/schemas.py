from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, StrictStr, StrictInt, field_validator
from datetime import datetime
from typing import Union

class CreateBody(BaseModel):
    seat_no: StrictInt
    passenger_name: StrictStr
    source: StrictStr
    destination: StrictStr
    date_input: datetime

    @field_validator("date_input")
    def check_date(cls, v: datetime):
        if v < datetime.now():
            raise ValueError("date_input must be in the future")
        return v


class UpdateBody(CreateBody):
    pass


# ----------- Response Model -----------
class ResponseModel(BaseModel):
    message: dict