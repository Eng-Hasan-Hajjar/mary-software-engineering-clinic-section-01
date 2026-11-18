backlog = [
    {"id": 1, "feature": "Register Patient", "priority": 1, "status": "To Do"},
    {"id": 2, "feature": "View Patients", "priority": 1, "status": "To Do"},
    {"id": 3, "feature": "Add Doctor", "priority": 2, "status": "To Do"},
    {"id": 4, "feature": "Book Appointment", "priority": 1, "status": "To Do"},
    {"id": 5, "feature": "Cancel Appointment", "priority": 2, "status": "To Do"},
    {"id": 6, "feature": "Daily Report", "priority": 3, "status": "To Do"}
]

sorted_backlog = sorted(backlog, key=lambda item: item["priority"])

print("--- Prioritized Backlog ---")
for item in sorted_backlog:
    print(item["feature"], "->", item["priority"])
