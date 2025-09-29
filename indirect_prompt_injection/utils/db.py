import os
from pathlib import Path
from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine, func, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

BASE_DIR = Path(__file__).resolve().parent.parent  # Get the root project directory
DB_PATH = BASE_DIR / "data" / "cv_data.db"  # Ensure the database is saved in the 'data' directory

# Ensure the parent directory of the database exists
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# Database URL
DB_URL = f"sqlite:///{DB_PATH}"

Base = declarative_base()
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)


class Cvs(Base):
    __tablename__ = "cv_entries"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)

    #results = relationship("ScreeningResult", back_populates="cv")

class JobListing(Base):
    __tablename__ = "job_listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    posted_at = Column(DateTime(timezone=True), server_default=func.now())

    #results = relationship("ScreeningResult", back_populates="job")

class ScreeningResult(Base):
    __tablename__ = "screening_results"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey('job_listings.id'))
    cv_id = Column(Integer, ForeignKey('cv_entries.id'))
    filename = Column(Text)
    evaluation = Column(Text)

    #job = relationship("JobListing", back_populates="results")
    #cv = relationship("CVEntry", back_populates="results")

# Ensure the database and tables are created
def create_db():
    # Connect to the engine and create tables
    with engine.connect() as conn:
        Base.metadata.create_all(bind=engine)  # This will create the tables if they don't exist
        print("Database and tables created successfully.")

# Call the function to create the database and tables
create_db()

