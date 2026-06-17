def user_schema(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "role": user["role"]
    }

def doctor_schema(doctor) -> dict:
    return {
        "id": str(doctor["_id"]),
        "name": doctor["name"],
        "specialization": doctor["specialization"],
        "availability_status": doctor["availability_status"]
    }

def patient_schema(patient) -> dict:
    return {
        "id": str(patient["_id"]),
        "name": patient["name"],
        "phone": patient["phone"],
        "email": patient["email"]
    }

def appointment_schema(appointment) -> dict:
    return {
        "id": str(appointment["_id"]),
        "patient_id": appointment["patient_id"],
        "doctor_id": appointment["doctor_id"],
        "appointment_date": appointment["appointment_date"],
        "appointment_time": appointment["appointment_time"],
        "status": appointment["status"]
    }