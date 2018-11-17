# Colors with Click
# pip install colorama (windows)

import click

@click.command()
@click.option('--name')
def main(name):
	click.echo(click.style(('Hello {}'.format(name)),fg='green'))
	click.secho('Hello world {}'.format(name),bg='red',fg='white')
	click.echo(click.style('ATTENTION', blink=True, bold=True))



if __name__ == '__main__':
	main()
