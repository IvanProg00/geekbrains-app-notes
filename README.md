# Notes

## About

The application "Notes" works from command line. It can create, read, update and
delete note.

## Usage

### Installation

```bash
pip3 install -r requirements.txt
```

### Commands

Create note:

```bash
python3 app.py create -t "Title" -m "Message"
```

Read notes:

```bash
python3 app.py read
```

Get note by ID:

```bash
python3 app.py get --id "61fd5d5b-84f6-4905-b8ce-730c30ce68d7"
```

Update note:

```bash
python3 app.py update \
  --id "cfedac1e-802f-4297-8871-b820f5a74eab" \
  --title "New Title" \
  -m "New Description"
```

Delete note:

```bash
python3 app.py delete --id "a9c2ba37-76ba-43b2-8c47-dd0c2021481d"
```
