import click
import service
from exception import ItemNotFound


@click.group()
def cli():
    pass


@click.command("create")
@click.option("-t", "--title", type=str, required=True, help="Title of the note.")
@click.option(
    "-m", "--message", type=str, required=True, help="Description of the note."
)
def create(title: str, message: str):
    """Create note."""
    service.create(title, message)


@click.command("read")
def read():
    """Read notes."""
    data = service.read()
    for val in data:
        print(f"id: {val['id']}")
        print(f"title: {val['title']}")
        print(f"message {val['message']}")
        print(f"created at: {val['created_at']}")
        print("--------------------")


@click.command("update")
@click.option("--id", type=str, required=True, help="ID of the note.")
@click.option("-t", "--title", type=str, required=True, help="Title of the note.")
@click.option(
    "-m", "--message", type=str, required=True, help="Description of the note."
)
def update(id: str, title: str, message: str):
    """Update note."""
    try:
        service.update(id, title, message)
    except ItemNotFound:
        print("element with specified id not found")


@click.command("delete")
@click.option("--id", type=str, required=True, help="ID of the note.")
def delete(id):
    """Delete note."""
    try:
        service.delete(id)
    except ItemNotFound:
        print("element with specified id not found")


cli.add_command(create)
cli.add_command(read)
cli.add_command(update)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
