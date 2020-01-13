# coding=utf-8
"""
Module reimplements set class for educational purposes.
"""

class Set:
        def __init__(self, value = []):
                self.data = []
                self.concat(value)

        def concat(self, value):
                for x in value:
                        if x not in self.data: # Powolne!
                                self.data.append(x)

        def union(self, other):
                res = self.data[:]
                for x in other:
                        if not x in res:
                                res.append(x)
                return Set(res)

        def intersect(self, other):
                res = []
                for x in other:
                        if x in other:
                                res.append(x)
                return Set(res)

        def __len__(self):
                return len(self.data)

        def __getitem__(self, key):
                return self.data[key]

        def __and__(self, other):
                return self.intersect(other)

        def __or__(self, other):
                return self.union(other)

        def __repr__(self):
                return f"Set: {repr(self.data)}"


if __name__ == '__main__':
    a = Set([12, 12, 13])
    print(a)

    b = Set([12, 14])
    print(b)

    print(a & b)

    print(a | b)

    print(len(a | b))
