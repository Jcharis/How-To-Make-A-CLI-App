import fire

class Hello:
	""" This is a simple class cli"""

	def hello(self,name):
		return 'Hello {} how are you'.format(name)


# greet = Hello()
# print(greet)
# # print(greet.hello("Paul"))

if __name__ == '__main__':
	greet = Hello()
	fire.Fire(greet)