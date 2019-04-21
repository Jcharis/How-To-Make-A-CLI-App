import fire

def greet(name):
	print('Hello {}'.format(name))


def bye(name):
	print('Good Bye  {}'.format(name))

def say(name):
	print('Say  {}'.format(name))


if __name__ == '__main__':
	fire.Fire({
		'greet':greet,
		'bye':bye,
		'say':say
		})


