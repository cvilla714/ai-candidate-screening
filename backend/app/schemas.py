from pydantic import BaseModel

# Base schema for candidates
class CandidateBase(BaseModel):
    name: str
    experience: float
    skills: str
    education: str
    certifications: str
    score: float

class CandidateCreate(CandidateBase):
    pass

class Candidate(CandidateBase):
    id: int

    class Config:
        orm_mode = True

# Schema for job description input
class JobDescription(BaseModel):
    description: str
