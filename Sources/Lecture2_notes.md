# Lecture 2 code to try
# Execute instructions below in interactive shell and analyse results


S = 'abcabc'

S[1:]

S

S[0:4]

S[:-1]

S[:]

S[::-1]

S + 'xyz'

S

S * 8

S * 2

S[0] = 'j'

S = 'j' + S[1:]

S

S.find('abca')

S.replace('abc', 'cdf')

S.upper()

S.lower()

S.isalpha()

line = 'aa, bb, cc, dd\n'

line.split(',')

line.rstrip()

'{0} lang'.format(S)

p_n = 'python'

f'{p_n}'

dir(S)

ord('a')

chr(ord('a'))

l = [1, 3, 2]

l.sort()

l

l.reverse()

l[99]

l[99] = 1

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[row[1] for row in m]

[row[1] + 1 for row in m]

[row[1] for row in m if not row[1] % 2]

diag = [m[i][i] for i in [0, 1, 2]]

[c * 2 for c in 'python']

G = (sum(row) for row in m)

next(G)
next(G)

list(map(sum, m))

{sum(row) for row in m}

{i: sum(m[i]) for i in range(3)}

[ord(x) for x in 'pypy']

{ord(x) for x in 'pypy'}

{x: ord(x) for x in 'pypy'}

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]

squares = []

for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)

squares

d = {'a': 1, 'b': 2, 'c':3}

'f' in d

'a' in d

d['a']

d['f']

d.keys()

list(d.items())

d.values()
