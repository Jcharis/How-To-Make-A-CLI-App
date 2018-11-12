import click

@click.command()
@click.option('--name',prompt=True,)


def main(name):
	click.echo(f"Your Name is {name} ")

if __name__ == '__main__':
	main()


# SECOND METHOD 
import click

@click.command()
@click.option('--name',prompt="Enter Your Firstname")

def main(name):
	click.echo(f"Your Name is {name}")

if __name__ == '__main__':
	main()


# THIRD METHOD
import click

@click.command()
@click.option('--name')


def main(name):
	fname = click.prompt("Enter Your Firstname")
	click.echo(f"Your Name is {name} and your firstname is {fname} ")

if __name__ == '__main__':
	main()



# WORKING WITH PASSWORD PROMPT
import click

@click.command()
@click.option('--name')
@click.option('--password',prompt=True,hide_input=True,confirmation_prompt=True)

def main(name,password):
	fname = click.prompt("Enter Your Firstname")
	click.echo(f"Your Name is {name} and your firstname is {fname} your password is {password} ")

if __name__ == '__main__':
	main()



# By Jesse JCharis - J-Secur1ty
# Jesus Saves @JCharisTech