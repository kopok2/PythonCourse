# coding=utf-8
"""
Class Tree printer module.
"""


def class_tree(cls, indent):
	"""
	Recursively print out class tree.

	Args:
		cls: class in tree.
		indent: current level of indentation.
	"""
	print('.' * indent, cls.__name__)
	for supercls in cls.__bases__:
		class_tree(supercls, indent + 3)


def instance_tree(inst):
	"""
	Print class tree for instance.

	Args:
		inst: instance of an object.
	"""
	print('Drzewo', inst)
	class_tree(inst.__class__, 3)


if __name__ == '__main__':
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E: pass
    class F(D, E): pass
    
    instance_tree(B())
    instance_tree(F())
    from person import Manager
    tom = Manager('Tomasz Czarny', 1000)
    instance_tree(tom)
    
    from collections import defaultdict
    instance_tree(defaultdict())
    
    
    
    
