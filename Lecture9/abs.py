from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
	def delegate(self):
		self.action()
	@abstractmethod
	def action(self):
		pass


class NonAbstract(Super):
    def action(self):
        print('OVERRIDE!!!')

if __name__ == '__main__':
    sup = NonAbstract()
    sup.delegate()