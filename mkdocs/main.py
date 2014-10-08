#!/usr/bin/env python
# coding: utf-8
import click
from mkdocs.build import build
from mkdocs.config import load_config
from mkdocs.gh_deploy import gh_deploy
from mkdocs.new import new
from mkdocs.serve import serve


@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--config-file', default='mkdocs.yml', type=click.Path(exists=True))
@click.pass_context
def cli(ctx, verbose, config_file):
    ctx.config = load_config(filename=config_file, options={
        'VERBOSE': verbose
    })


@cli.command(name='serve')
@click.pass_context
def serve_command(ctx):
    serve(ctx.config)


@cli.command(name='build')
@click.pass_context
def build_command(ctx):
    print ctx
    build(ctx.config)


@cli.command(name='json')
@click.pass_context
def json_command(ctx):
    print ctx
    build(ctx.config, dump_json=True)


@cli.command(name='gh-deploy')
@click.pass_context
def gh_deploy_command(ctx):
    gh_deploy(ctx.config)


@cli.command(name='new')
@click.argument('directory-name')
def new_command(directory_name):
    new(directory_name)

if __name__ == '__main__':
    cli()
