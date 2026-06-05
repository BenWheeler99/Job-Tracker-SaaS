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
    notes: Optional[str] = None
    date_applied: Optional[str] = None


# first pydantic would run any pre-processing and validation on the input data, ensuring that it adheres to the defined schema.
# Then, it would convert the validated data into a format that can be easily used by the application, such as a dictionary or an instance of the Job class. 
# Finally, it would return the processed data, which can be used for further operations like database interactions or API responses.