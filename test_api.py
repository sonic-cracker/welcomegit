import requests
from datetime import date

BASE_URL = "http://localhost:8000"

def test_api():
    # Create a doctor
    doctor_data = {
        "name": "Dr. Smith",
        "specialization": "Cardiology"
    }
    response = requests.post(f"{BASE_URL}/doctors/", json=doctor_data)
    print("Created doctor:", response.json())

    # Create a patient
    patient_data = {
        "name": "John Doe",
        "age": 45,
        "diagnosis": "Heart condition",
        "admission_date": str(date.today()),
        "doctor_id": 1
    }
    response = requests.post(f"{BASE_URL}/patients/", json=patient_data)
    print("Created patient:", response.json())

    # Get all patients
    response = requests.get(f"{BASE_URL}/patients/")
    print("All patients:", response.json())

    # Get patients for a specific doctor
    response = requests.get(f"{BASE_URL}/doctors/1/patients")
    print("Doctor's patients:", response.json())

    # Test error handling
    try:
        response = requests.get(f"{BASE_URL}/patients/999")
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error as expected: {err}")

if __name__ == "__main__":
    test_api()