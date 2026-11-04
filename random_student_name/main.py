
import json
import secrets
from pathlib import Path

# First Group - 17 Students
students = [
    "Zahraa Badawi",
    "Raneem Al-Hasram",
    "Nihad Hamsho",
    "Nada Zuwain",
    "Aya Nehmeh",
    "Haya Nehmeh",
    "Maria Al-Ibrahim",
    "Shatha Al-Abdo",
    "Wafaa Muhaysin",
    "Israa Al-Khalil",
    "Rola Qaddour",
    "Safa Moallem",
    "Asia Al-Khazou",
    "Hadeel Qarbi",
    "Ghaziya Al-Aboud",
    "Bayan Raslan",
    "Lama Waqqas",
]

state_file = Path(__file__).with_name(
    "first_group_picker_state.json"
)

try:
    data = json.loads(
        state_file.read_text(encoding="utf-8")
    )
    remaining = data["remaining"]

    if (
        not isinstance(remaining, list)
        or len(remaining) != len(set(remaining))
        or not set(remaining).issubset(students)
    ):
        remaining = []

except (FileNotFoundError, OSError, ValueError,
        KeyError, TypeError):
    remaining = []

# Start a new round after selecting everyone
if not remaining:
    remaining = students.copy()

# Fair random selection
selected = secrets.choice(remaining)
remaining.remove(selected)

# Save remaining students
state_file.write_text(
    json.dumps({"remaining": remaining}, indent=2),
    encoding="utf-8"
)

print(selected)
