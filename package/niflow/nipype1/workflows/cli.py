import click
from . import __version__

@click.command()
@click.version_option(__version__)
def main():
    print("CLI access to Nipype 1 workflows is not yet supported")
