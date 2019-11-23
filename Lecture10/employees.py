# coding=utf-8
"""
Employees module.
"""


class Employee:
	def __init__(self, name, salary=0):
		self.name = name
		self.salary = salary
	def give_raise(self, percent):
		self.salary *= (1 + percent)
	def work(self):
		print(f'{self.name} pracuje.')
	def __repr__(self):
		return f'Pracownik: {self.name}, wynagrodzenie: {self.salary}'


class Chef(Employee):
	def __init__(self, name):
		Employee.__init__(self, name, 50000)
	def work(self):
		print(f'{self.name} przygotowuje jedzenie.')


class Server(Employee):
	def __init__(self, name):
		Employee.__init__(self, name, 50000)
	def work(self):
		print(f'{self.name} obsługuje klienta.')


class PizzaRobot(Chef):
	def __init__(self, name):
		Chef.__init__(self, name)
	def work(self):
		print(f'{self.name} przygotowuje pizzę')


if __name__ == '__main__':
	bob = PizzaRobot('Robert')
	print(bob)
	bob.give_raise(.10)
	print(bob)
