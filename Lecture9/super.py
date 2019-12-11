print(super)

class A:
	def __init__(self, val):
		self.val = val

class B(A):
	def __init__(self):
		super().__init__(12)
b = B()
print(b.val)
