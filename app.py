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
    service.create(title, message)


@click.command("read")
def read():
    data = service.read()
    for val in data:
        print(f"id: {val['id']}")
        print(f"title: {val['title']}")
        print(f"message {val['message']}")
        print(f"created at: {val['created_at']}")
        print("--------------------")


cli.add_command(create)
cli.add_command(read)

if __name__ == "__main__":
    cli()
