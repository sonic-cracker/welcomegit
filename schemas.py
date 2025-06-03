from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class DoctorBase(BaseModel):
    name: str
    specialization: Optional[str] = None

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PatientBase(BaseModel):
    name: str
    age: int
    diagnosis: str
    admission_date: date
    doctor_id: Optional[int] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    doctor: Optional[Doctor] = None
    model_config = ConfigDict(from_attributes=True)