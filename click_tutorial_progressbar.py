
# Working with progressbar
import click

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def main(count, name):
    """This script prints hello NAME COUNT times."""
    # for x in range(count):
    #     click.echo('Hello %s!' % name)

    
    with click.progressbar(range(count),label="Initializing ") as bar:
     	for x in bar:
     		click.secho('Hello %s!' % name,bg='red')

if __name__ == '__main__':
	main()



# Jesse JCharis
# Jesus Saves @JCharisTech