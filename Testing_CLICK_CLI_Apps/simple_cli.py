import click


@click.group()
def main():
    pass

@main.command()
@click.argument('text')
def say(text):
	click.echo('You said {}'.format(text.title()))

@main.command()
@click.argument('name')
def greet(name):
	click.echo('Hello {}'.format(name))
    

if __name__ == "__main__":
    main()