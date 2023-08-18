import json
import uuid
from pathlib import Path
from datetime import datetime

FILE_NAME = "notes.json"


def create(title, message):
    data = []
    file = Path(FILE_NAME)
    if file.is_file():
        with open(FILE_NAME, "r") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError as e:
                pass

    note = {
        "id": str(uuid.uuid4()),
        "title": title,
        "message": message,
        "created_at": str(datetime.now()),
    }

    data.append(note)

    with open(FILE_NAME, "w") as f:
        json.dump(data, f)