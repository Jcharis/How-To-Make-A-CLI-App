import click

@click.command()
@click.argument('number1',type=int)
@click.argument('number2',type=int)
@click.argument('method',default='add')


def main(number1,number2,method):
	""" Add Number 1 and Number 2"""
	if method == 'add':
		result = number1 + number2
	elif method == 'substract':
		result = number1 - number2
	elif method == 'multiply':
		result = number1 * number2
	click.echo(result)

# Multiple Argument - Variadic Arguments
@click.command()
@click.argument('source',nargs=-1)
@click.argument('destination',nargs=1)

def main(source,destination):
	for f in source:
		click.echo('Moving {} to Folder {}'.format(f,destination))



if __name__ == '__main__':
	main()




# By Jesse JCharis - J-Secur1ty
# Jesus Saves @JCharisTech