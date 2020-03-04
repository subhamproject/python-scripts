#!/usr/bin/python2.7

import click
import sys
import os
import configparser
from github import Github
from click_shell import shell


@shell(prompt='Manage/Github > ', intro='Staring Github Control Framework...')
def main():
    pass


@main.command()
@click.option('-r','--repo',help='Please provide repo names,comma seperated for multiple!')
@click.option('-u','--user',help='Please provide user names,comma seperated for multiple!')
@click.option('-c','--config',default=os.path.join(os.path.expanduser("~"), '.config', 'config.ini'),help='Not mandatory')
def delete(repo,user,config):
    if not os.path.exists(config):
       click.echo('config file: {} does not exits,Please configure'.format(config))
       sys.exit()

    configs = configparser.ConfigParser()
    configs.read(config)

    if repo and user:
       reponames = repo.split(',')
       users = user.split(',')
    else:
       click.echo("Please provide repo and user name, '-r','--repo' & '-u','--user'")
       sys.exit()

    if repo.startswith('subham'):
       token = configs['first']['token']
    else:
       token = configs['second']['token']

    g = Github(token)
    for un in users:
       for rn in reponames:
           try:
              rp = g.get_repo(rn)
              if rp.has_in_collaborators(un):
                 click.echo('Deleting {} from this Repo :: {}'.format(un,rn))
                 rp.remove_from_collaborators(un)
              else:
                 click.echo('User:: {} does not exist in this repo:: {}'.format(un,rn))
           except StopIteration:
                 click.echo('Count not delete user {} from repo :: {}'.format(un,rp))
    return

@main.command()
@click.option('-r','--repo',help='Please provide repo names,comma seperated for multiple!')
@click.option('-u','--user',help='Please provide user names,comma seperated for multiple!')
@click.option('-c','--config',default=os.path.join(os.path.expanduser("~"), '.config', 'config.ini'),help='Not mandatory')
def add(repo,user,config):
    if not os.path.exists(config):
       click.echo('config file {} does not exits,Please configure'.format(config))
       sys.exit()

    configs = configparser.ConfigParser()
    configs.read(config)

    if repo and user:
       reponames = repo.split(',')
       users = user.split(',')
    else:
        click.echo("Please provide repo and user name, '-r','--repo' & '-u','--user'")
        sys.exit()

    if repo.startswith('subham'):
       token = configs['first']['token']
    else:
       token = configs['second']['token']

    g = Github(token)
    for un in users:
       for rn in reponames:
          try:
            rp = g.get_repo(rn)
            if rp.has_in_collaborators(un):
               click.echo('User:: {} already added for this repo:: {}, skipping...!'.format(un,rn))
            else:
               click.echo('Adding {} to this Repo :: {}'.format(un,rn))
               rp.add_to_collaborators(un,permission='push')
          except StopIteration:
            click.echo('Count not add user {} to repo :: {}'.format(un,rp))
    return


if __name__ == '__main__':
   main()
