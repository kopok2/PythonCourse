---
title:
- Akademia Pythona
author:
- Materiały uzupełniające
theme:
- Copenhagen
---


# KN Pythona - Kurs Pythona

KN Pythona wita na kursie Pythona.

Plan:

+ Nowości w Pythonie 3.8


# Python 3.8

Walrus operator

```python
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, 
	  expected <= 10)")
```


# Python 3.8

Walrus operator

```python
discount = 0.0
if (mo := re.search(r'(\d+)% discount', advertisement)):
    discount = float(mo.group(1)) / 100.0
```


# Python 3.8

Walrus operator

```python
# Loop over fixed length blocks
while (block := f.read(256)) != '':
    process(block)
```


# Python 3.8

Walrus operator

```python
[clean_name.title() for name in names
 if (clean_name := normalize('NFC', name))
     in allowed_names]
```


# Python 3.8

Positional only arguments

```python
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
```

# Python 3.8

Positional only arguments

```python
def pow(x, y, z=None, /):
    "Emulate the built in pow() function"
    r = x ** y
    return r if z is None else r%z
```
