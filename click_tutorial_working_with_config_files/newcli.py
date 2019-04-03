import click
import click_config_file

@click.command()
@click.option('--name','-n', default='Jesse', help='Specify Name')
@click.option('--salary','-s')
@click_config_file.configuration_option()
def main(name,salary):
    click.echo('Hello {} Your salary is {}.'.format(name,salary))



if __name__ == '__main__':
	main()
