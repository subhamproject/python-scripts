#!/usr/bin/python3

import click
import click_shell
from click_shell import shell

@shell(prompt='jenkins > ', intro='Starting my app...')
def main():
   pass

@main.command()
@click.option('--name')
def reverse():
  pass

@main.command()
@click.option('--sir')
def on(sir):
  click.echo(sir)

@main.command()
@click.argument('mandal',default='kiko')
def off():
  pass


if __name__ == '__main__':
 main()
