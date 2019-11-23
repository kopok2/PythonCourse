# coding=utf-8
"""
Pizzeria module.
"""

from employees import Server, PizzaRobot

class Customer:
	def __init__(self, name):
		self.name = name
	def order(self, server):
		print(f'{self.name} zamawia od {server}')
	def pay(self, server):
		print(f'{self.name} płaci {server}')


class Oven:
	def bake(self):
		print('Piec piecze')


class PizzaShop:
    def __init__(self):
        self.server = Server('Ernest')
        self.chef = PizzaRobot('Robert')
        self.oven = Oven()
    
    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == '__main__':
	scene = PizzaShop()
	scene.order('Amadeusz')
	print('#' * 64)
	scene.order('Aleksander')
