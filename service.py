import json
import uuid
from pathlib import Path
from datetime import datetime
from typing import List
from exception import ItemNotFound

FILE_NAME = "notes.json"


def create(title: str, message: str):
    data = get_list()

    note = {
        "id": str(uuid.uuid4()),
        "title": title,
        "message": message,
        "created_at": datetime.now().isoformat(),
    }

    data.append(note)

    with open(FILE_NAME, "w") as f:
        json.dump(data, f)


def read() -> List[dict]:
    data = get_list()
    data.sort(
        key=lambda x: datetime.fromisoformat(x["created_at"]).timestamp(), reverse=True
    )

    return data


def update(id: str, title: str, message: str):
    data = get_list()

    for i in range(len(data)):
        if data[i]["id"] == id:
            data[i].update({"title": title, "message": message})
            break
    else:
        raise ItemNotFound

    with open(FILE_NAME, "w") as f:
        json.dump(data, f)


def delete(id: str):
    data = get_list()

    for i in range(len(data)):
        if data[i]["id"] == id:
            data.pop(i)
            break
    else:
        raise ItemNotFound

    with open(FILE_NAME, "w") as f:
        json.dump(data, f)


def get_list() -> List[dict]:
    data = []
    file = Path(FILE_NAME)
    if file.is_file():
        with open(FILE_NAME, "r") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError as e:
                pass

    return data
