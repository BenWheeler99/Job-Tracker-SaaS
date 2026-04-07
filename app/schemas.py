from typing import Optional, Literal
from pydantic import BaseModel


class Job(BaseModel):
    id: Optional[int] = None
    name: str
    company: str = None
    state: Literal["applied", "Rejected", "offered"]
    offer: Optional[bool] = None


    