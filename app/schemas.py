# Pydantic schema defines the structure of the data that will be 
# accepted and returned by the API endpoints.

from typing import Optional, Literal
from pydantic import BaseModel

# Pydantic model for data validation and serialization for the Job entity. 
# This model defines the structure of the data that will be accepted and 
# returned by the API endpoints.

class Job(BaseModel):
    id: Optional[int] = None
    name: str
    company: str = None
    state: Literal["Applied", "Rejected", "Offered"]
    offer: Optional[bool] = None


    