# Notes

## About

The application "Notes" works from command line. It can create, read, update and
delete note.

## Usage

Create note:

```bash
python3 app.py create -t "Title 1" -m "Message"
```

Read notes:

```bash
python3 app.py read
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
