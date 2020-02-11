#!/usr/bin/python3

import click

@click.command()
@click.option('--name','-n',default='Subham',help='Please provide your name')
@click.option('--multi','-m',nargs=2)
@click.argument('sir',default='apple')


def main(name,multi,sir):
  click.echo('Hello world,my name is {}'.format(name))
  click.echo(multi)
  click.echo(sir)

if __name__ == '__main__':
  main()
