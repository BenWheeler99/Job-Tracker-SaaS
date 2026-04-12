from typing import Optional
from sqlalchemy import Boolean, String
from sqlalchemy.orm import mapped_column, Mapped
from app.database import Base

# an example mapping using the base
# Nullable = FALSE by default
class Job_schema(Base):
    __tablename__ = "Jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    company: Mapped[str] = mapped_column(String(30), nullable=True)
    state: Mapped[Optional[str]]
    offer: Mapped[bool] = mapped_column(Boolean, default=True)
    
    