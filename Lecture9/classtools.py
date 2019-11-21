# coding=utf-8
"""
Universal module for class attributes string representation.
"""


class AttrDisplay:
	"""
	Universal mixin for class display.
	"""
	def _gather_attrs(self):
		"""
		Collect all instance attributes.

		Retuns:
			Attributes string representation.
		"""
		attrs = []
		for key in sorted(self.__dict__):
			attrs.append(f'{key}: {getattr(self, key)}')
		return '\n'.join(attrs)

	def __str__(self):
		return '{0}\n{1}'.format(self.__class__.__name__, self._gather_attrs())
