board = {
    "To Do": ["Register Patient", "View Patients", "Book Appointment"],
    "In Progress": ["Validate Patient Data"],
    "Done": ["Project Setup"]
}


def show_board():
    for column, tasks in board.items():
        print("\n" + column)
        for task in tasks:
            print(" -", task)

show_board()
