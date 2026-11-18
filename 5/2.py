patients = []

def register_patient(name, phone):
    if not name.strip():
        return None

    patient = {
        "name": name.strip(),
        "phone": phone.strip()
    }
    patients.append(patient)
    return patient


def view_patients():
    if not patients:
        print("No patients found.")
        return

    print("--- Patients ---")
    for index, patient in enumerate(patients, start=1):
        print(index, patient["name"], "-", patient["phone"])

register_patient("Ahmad", "0991111111")
register_patient("Sara", "0992222222")
view_patients()

backlog = [
    {"id": 1, "feature": "Register Patient", "priority": 1, "status": "To Do"},
    {"id": 2, "feature": "View Patients", "priority": 1, "status": "To Do"},
    {"id": 3, "feature": "Add Doctor", "priority": 2, "status": "To Do"},
    {"id": 4, "feature": "Book Appointment", "priority": 1, "status": "To Do"},
    {"id": 5, "feature": "Cancel Appointment", "priority": 2, "status": "To Do"},
    {"id": 6, "feature": "Daily Report", "priority": 3, "status": "To Do"}
]

sprint_backlog = sorted(backlog, key=lambda item: item["priority"])[:3]

print("--- Sprint Backlog ---")
for item in sprint_backlog:
    print(item["id"], item["feature"])
