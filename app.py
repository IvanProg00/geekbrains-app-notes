import click
import service


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


@click.command("delete")
@click.option("--id", type=str, required=True, help="ID of the note.")
def delete(id):
    """Delete note."""
    service.delete(id)


cli.add_command(create)
cli.add_command(read)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
