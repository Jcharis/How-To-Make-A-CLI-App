import click

@click.command()
# basic options
@click.option('--name','-n',default='John',help='Firstname description')

# Multiple Values
@click.option('--salary','-s',nargs=2,help='Your Monthly Salary',type=int)

# Multiple Options
@click.option('--location','-l',help="Places You ve Visited",multiple=True)

def main(name,salary,location):
	click.echo('Hello World My Name is {},My Salary is {}'.format(name,sum(salary)))
	click.echo('\n'.join(location))



if __name__ == '__main__':
	main()