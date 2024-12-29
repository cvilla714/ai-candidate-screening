
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Candidate(Base):
    __tablename__ = "candidates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    experience = Column(Float)
    skills = Column(String)
    education = Column(String)
    certifications = Column(String)
    score = Column(Float)