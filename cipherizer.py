# Reverse A string
# Leet conversion
# Shuffling
import click
import random

@click.group()
def main():
	pass

@main.command()
@click.argument('text')
def reverse(text):
	""" Reverse A Text """
	click.echo(text[::-1])

@main.command()
@click.argument('text')
def leet(text):
	""" leet A Text """
	chars = {'a':'4','b':'l3','c':'','d':'[', 'e':'3','l':'1','s':'5','t':'7', 'w':'\/\/','o':'0', 't':'+'}
	getchar = lambda c: chars[c] if c in chars else c 
	click.echo(''.join(getchar(c) for c in text))



@main.command()
@click.argument('myword')
def shufflize(myword):
	""" shufflize A Text """
	click.echo(''.join(random.sample(myword,len(myword))))




if __name__ == '__main__':
	main()


# By Jesse JCharis -J-Secur1ty
# Jesus Saves @JCharisTech