from pydantic import BaseModel
from datetime import datetime


class DataModel(BaseModel):
    url: str
    created: datetime
    edited: datetime
