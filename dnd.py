"""
Dungeons and Dragons 5th ed. CLI Script

This is a helper script for playing DnD 5e games that comes
with a number of features to make playing smoother:

item: does a lookup of an item and returns ones that match
    the given text.

trinket: randomly returns a trinket from a number of tables
"""

import click

__version__ = "0.0.1"


@click.group()
def dnd() -> None:
    pass


@dnd.command()
@click.option(
    '-n', '--name', 'name',
    required=True, type=str,
    help='the name of the item to search for')
def item(name: str) -> None:
    click.echo(f'Items that contain {name}:')


@dnd.command()
@click.option(
    '-n', '--name', 'name',
    required=True, type=str,
    help='the name of the spell to search for')
def spell(name) -> None:
    click.echo(f'Spells that contain {name}:')


@dnd.command()
@click.option('-c', '--count', default=1, help='number of trinkets to return')
@click.option('-t', '--table', default=1, help='table number to choose from')
def trinket(count: int, table: int) -> None:
    click.echo(f'Random trinket{"s" if count > 1 else ""} from table {table}: ')

    for _ in range(count):
        click.echo("trinket name")


@dnd.command()
def version() -> None:
    click.echo(f'v{__version__}')


if __name__ == '__main__':
    dnd()
