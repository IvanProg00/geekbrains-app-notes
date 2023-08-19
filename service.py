import json
import uuid
from pathlib import Path
from datetime import datetime
from typing import List
from exception import ItemNotFound

FILE_NAME = "notes.json"


def create(title: str, message: str):
    data = read()

    note = {
        "id": str(uuid.uuid4()),
        "title": title,
        "message": message,
        "created_at": str(datetime.now()),
    }

    data.append(note)

    with open(FILE_NAME, "w") as f:
        json.dump(data, f)


def read() -> List[dict]:
    data = []
    file = Path(FILE_NAME)
    if file.is_file():
        with open(FILE_NAME, "r") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError as e:
                pass

    return data


def update(id: str, title: str, message: str):
    data = read()

    for i in range(len(data)):
        if data[i]["id"] == id:
            data[i].update({"title": title, "message": message})
            break
    else:
        raise ItemNotFound

    with open(FILE_NAME, "w") as f:
        json.dump(data, f)


def delete(id: str):
    data = read()

    for i in range(len(data)):
        if data[i]["id"] == id:
            data.pop(i)
            break
    else:
        raise ItemNotFound

    with open(FILE_NAME, "w") as f:
        json.dump(data, f)
