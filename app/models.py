from typing import Optional
from sqlalchemy import Boolean, Integer, String, ForeignKey, create_engine, text
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
import os
from dotenv import load_dotenv


load_dotenv()

# This is a section establishing POSTGRESQL server connection using hidden credentials
# credentials in .env file and being gitignored. 
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

#calling database connection
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

#testing connection
with engine.connect() as conn:
    result = conn.execute(text("SELECT 'Connection Successful'"))
    print(result.fetchone())

# The below section is for defining a model for how our webpage will speak to PostgreSQL. 
# This model is essentially a schema for how our database will be constructed. 

# declarative base class
class Base(DeclarativeBase):
    pass

# an example mapping using the base
# Nullable = FALSE by default
class Job_schema(Base):
    __tablename__ = "Jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    company: Mapped[str] = mapped_column(String(30))
    state: Mapped[Optional[str]]
    offer: Mapped[bool] = mapped_column(Boolean, default=True)

# Create all tables in the database based on the declarative base
Base.metadata.create_all(engine)