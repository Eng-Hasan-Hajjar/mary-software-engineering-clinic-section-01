patients = []

def register_patient(name, phone):
    patient = {
        "name": name,
        "phone": phone
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
