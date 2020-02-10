#!/usr/bin/env python

"""
Dungeons and Dragons 5th ed. CLI Script

This is a helper script for playing DnD 5e games that comes
with a number of features to make playing smoother:

al: adventure league specific information

background: info related to player backgrounds

item: does a lookup of an item and returns ones that match
    the given text.

name: generates a random name

trinket: randomly returns a trinket from a number of tables
"""

import click
from random import choice

__version__ = "0.0.1"


@click.group()
def dnd() -> None:
    pass


@dnd.command()
@click.argument('search_phrase', required=True, type=str)
def item(search_phrase: str) -> None:
    click.echo(f'Items that contain the phrase {search_phrase}:')


@dnd.command()
@click.argument('search_phrase', required=True, type=str)
def monster(search_phrase: str) -> None:
    click.echo(f'Monsters that contain the phrase {search_phrase}:')


@dnd.command()
def name() -> None:
    click.echo('stinky pete')


@dnd.command()
@click.argument('search_phrase', required=True, type=str)
def spell(search_phrase: str) -> None:
    click.echo(f'Spells that contain the phrase {search_phrase}:')


@dnd.command()
@click.option('-c', '--count', default=1, help='number of trinkets to return')
@click.option('-t', '--table', default=1, type=click.IntRange(1, 12),
              help='table number to choose from')
def trinket(count: int, table: int) -> None:
    click.echo(
        f'{count} random trinket{"s" if count > 1 else ""} from table #{table}:'
    )
    with open(f'./tables/trinkets/{table}.txt', 'r') as trinket_file:
        trinkets = trinket_file.readlines()

    for _ in range(count):
        click.echo(choice(trinkets).strip())


@dnd.command()
def version() -> None:
    """
    returns the current version of dnd-cli
    """
    click.echo(f'v{__version__}')


if __name__ == '__main__':
    dnd()
