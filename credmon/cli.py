# -*- coding: utf-8 -*-

import click
import yaml
import importlib

from io import open

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


@click.group()
def cli():
    '''Utility for checking credentials.'''
    pass


@cli.command()
@click.argument('config_path', type=click.Path(exists=True))
def check(config_path):
    '''Check credentials.'''
    config = yaml.load(open(config_path, 'r'), Loader=Loader)

    for index, item in enumerate(config['checks']):
        driver  = importlib.import_module('credmon.drivers.{}'.format(item['type'].lower()))
        check = getattr(driver, 'Check{}'.format(item['type'].title()))(**item['config'])

        try:
            if check.check():
                click.secho('{}: Check {} {} successful.'.format(index, item['name'], item['type']), fg='green')
            else:
                click.secho('{}: Check {} {} failed.'.format(index, item['name'], item['type']), fg='red')
        except Exception as err:
            click.secho('{}: Check {} {} failed. Error: {}'.format(index, item['name'], item['type'], str(err)), fg='red')


if __name__ == '__main__':
    cli()
