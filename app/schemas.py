from typing import Optional
from pydantic import BaseModel


class Job(BaseModel):
    id: Optional[int] = None
    name: str
    company: str = None
    state: str = None
    offer: Optional[bool] = None

    