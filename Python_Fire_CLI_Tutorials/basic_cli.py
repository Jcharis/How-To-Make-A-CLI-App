# Method 1
import fire

def greet(name):
	print('Hello {}'.format(name))


if __name__ == '__main__':
	fire.Fire()


# Method 2

import fire

def greet(name):
	print('Hello {}'.format(name))


if __name__ == '__main__':
	fire.Fire(greet)