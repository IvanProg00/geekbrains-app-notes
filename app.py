import click
import service


@click.group()
def cli():
    pass


@click.command("create")
@click.option("-t", "--title", type=str, required=True, help="Title of the note.")
@click.option(
    "-d", "--description", type=str, required=True, help="Description of the note."
)
def create(title, description):
    service.create(title, description)


cli.add_command(create)

if __name__ == "__main__":
    cli()
