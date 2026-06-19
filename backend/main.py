from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import db
from models import User, Doctor, Patient, Appointment
from schemas import user_schema, doctor_schema, patient_schema, appointment_schema
from bson import ObjectId
import os
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── ROOT ───
@app.get("/")
def root():
    return {"message": "Hospital Appointment System API is running"}

# ─── AUTH ───
@app.post("/register")
async def register(user: User):
    await db["users"].insert_one(user.dict())
    return {"message": "User registered successfully"}

@app.post("/login")
async def login(user: User):
    found = await db["users"].find_one({"email": user.email, "password": user.password})
    if found:
        return {"message": "Login successful", "role": found["role"]}
    return {"message": "Invalid credentials"}

# ─── DOCTORS ───
@app.post("/doctors")
async def add_doctor(doctor: Doctor):
    await db["doctors"].insert_one(doctor.dict())
    return {"message": "Doctor added"}

@app.get("/doctors")
async def get_doctors():
    doctors = await db["doctors"].find().to_list(100)
    return [doctor_schema(d) for d in doctors]

@app.put("/doctors/{id}")
async def update_doctor(id: str, doctor: Doctor):
    await db["doctors"].update_one({"_id": ObjectId(id)}, {"$set": doctor.dict()})
    return {"message": "Doctor updated"}

@app.delete("/doctors/{id}")
async def delete_doctor(id: str):
    await db["doctors"].delete_one({"_id": ObjectId(id)})
    return {"message": "Doctor deleted"}

# ─── PATIENTS ───
@app.post("/patients")
async def add_patient(patient: Patient):
    await db["patients"].insert_one(patient.dict())
    return {"message": "Patient added"}

@app.get("/patients")
async def get_patients():
    patients = await db["patients"].find().to_list(100)
    return [patient_schema(p) for p in patients]

# ─── APPOINTMENTS ───
@app.post("/appointments")
async def add_appointment(appointment: Appointment):
    await db["appointments"].insert_one(appointment.dict())
    return {"message": "Appointment booked"}

@app.get("/appointments")
async def get_appointments():
    appointments = await db["appointments"].find().to_list(100)
    return [appointment_schema(a) for a in appointments]

@app.put("/appointments/{id}")
async def update_appointment(id: str, appointment: Appointment):
    await db["appointments"].update_one({"_id": ObjectId(id)}, {"$set": appointment.dict()})
    return {"message": "Appointment updated"}

@app.delete("/appointments/{id}")
async def delete_appointment(id: str):
    await db["appointments"].delete_one({"_id": ObjectId(id)})
    return {"message": "Appointment deleted"}

# ─── DASHBOARD ───
@app.get("/dashboard-stats")
async def dashboard_stats():
    doctors = await db["doctors"].count_documents({})
    patients = await db["patients"].count_documents({})
    appointments = await db["appointments"].count_documents({})
    return {"doctors": doctors, "patients": patients, "appointments": appointments}

# ─── START SERVER ───
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)