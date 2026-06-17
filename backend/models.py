from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    password: str
    role: str

class Doctor(BaseModel):
    name: str
    specialization: str
    availability_status: str

class Patient(BaseModel):
    name: str
    phone: str
    email: str

class Appointment(BaseModel):
    patient_id: str
    doctor_id: str
    appointment_date: str
    appointment_time: str
    status: str