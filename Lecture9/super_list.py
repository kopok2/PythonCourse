from classtools import AttrDisplay

class SuperList(list, AttrDisplay):
	pass


sl = SuperList()
print(SuperList)