---
title:
- Akademia Pythona
author:
- VIII Zagadnienia zaawansowane
theme:
- Copenhagen
---


# KN Pythona - Kurs Pythona

KN Pythona wita na kursie Pythona.

Plan:

+ Dekoratory



# Dekoratory

Dotychczas:

- @property
- @abstractmethod
- @classmethod
- @staticmethod


# Dekoratory

Dekoratory to obiekty wywoływalne.



# Dekoratory

Dekoracja jest sposobem określania kodu zarządzającego dla funkcji oraz klas.



# Dekoratory

Dekoracja przetwarza obiekty wywoływalne (funkcje oraz klasy). Dekorator dodaje instrukcje wykonywalne po kodzie obiektów.


# Zarządzanie

Dekoratory mogą zarządzać wywołaniami oraz instancjami. 


# Dekoratory

Dekoracja zachodzi poprzez ponowne dowiązanie nazw przetwarzanych obiektów.


# Dekoratory

```python
@decorator
def F(arg):
	...
F(99)

def F(arg):
	...
F = decorator(F)
F(99)

```


# Cechy dekoratorów

Cechy dekoratorów:

- Niska powtarzalność
- Strukturyzacja i hermetyzacja
- Jawność i czytelność


# Dekoratory funkcji

```python
func(6, 7) # udekorowana funkcja
decorator(func)(6, 7) # dekorator zwraca obiekt
```


# Dekoratory funkcji

```python
def decorator(F):
	return F
@decorator
def func(a, b):
	...
```



# Dekoratory funkcji

```python
def decorator(F):
	# zapisanie lub użycie F
	# zwrócenie innego obiektu
```


# Dekoratory funkcji

```python
def decorator(F):
	def wrapper(*args):
		# użycie F oraz args
		# F(*args)
	return wrapper
```


# Dekoratory funkcji

```python
class decorator:
	def __init__(self, func):
		self.func = func
	def __call__(self, *args):
		# użycie self.func oraz args
		# self.func(*args)
```



# Dekoratory metod

Powyższy kod nie udekoruje poprawnie metody klasy.



# Dekoratory metod

```python
class C:
	@decorator
	def method(self, x, y):
		...
```


# Dekoratory klas

```python
@decorator
class C:
	...
x = C(99)
```


# Dekoratory klas

```python
class C:
	...
C = decorator(C)
x = C(99)
```


# Dekoratory klas

```python
def decorator(C):
	# przetworzenie klasy C
	return C
```


# Dekoratory klas

```python
def decoratory(C):
	# zapisanie lub przetworzenie C
	# zwrócenie klasy
```


# Dekoratory klas

```python
def decorator(cls):
	class Wrapper:
		def __init__(self, *args):
			self.wrapped = cls(*args)
		def __getattr__(self, name):
			return getattr(self.wrapped, name)
	reutrn Wrapper
```


# Dekoratory klas

```python
class Decorator: # tylko jedna instancja!
	def __init__(self, C):
		self.C = C
	def __call__(self, *args):
		self.wrapped = self.C(*args)
		return self
	def __getattr__(sefl, name):
		return getattr(self.wrapped, name)
```


# Dekoratory klas

```python
class Wrapper: ...
def decorator(cls):
	def on_call(*args):
		return Wrapper(C(*args))
	return on_call
```


# Zagnieżdżanie dekoratorów

```python
@A
@B
@C
def f(...):
	...
def f(..):
	...
f = A(B(C(f)))
```


# Zagnieżdżanie dekatorów

```python
def d1(F): return lambda: 'a' + F()
def d2(F): return lambda: 'b' + F()
def d3(F): return lambda: 'c' + F()
@d1
@d2
@d3
def func():
	return 'd'
print(func()) # abcd
```


# Argumenty dekoratorów

```python
@decorator(A, B)
def F(arg):
	...
F(99)
```


# Argumenty dekoratorów

```python
def F(arg):
	...
F = decorator(A, B)(F)
F(99)
```


# Argumenty dekoratorów

```python
def decorator(A, B):
	# zapisanie lub użycie A i B
	def actual_decorator(F):
		# zapisanie lub użycie F
		# zwrócenie obiektu
		return callable
	return actual_decorator
```


# Śledzenie wywołań

```python
class tracer:
	def __init__(self, func):
		self.calls = 0
		self.func = func
	def __call__(self, *args):
		sefl.calls += 1
		print(f"Wywołanie {self.func.__name__}" +\ 
		       " nr {self.calls}")
		sefl.func(*args)
@tracer
def spam(a, b, c):
	print(a, b, c)
```


# Śledzenie wywołań 2

```python
class tracer:
	def __init__(self, func):
		self.func = func
	def __call__(self, *args, **kwargs):
		return self.func(*args, **kwargs)
```


# Zakresy zawierające, tzw. closures

```python
calls = 0
def tracer(func):
	def wrapper(*args, **kwargs):
		global calls
		calls += 1
		print(calls)
		return func(*args, **kwargs)
	return wrapper # do obiektu dołączony jest zakres
```


# Dekoracja przy użyciu deskryptorów

```python
class tracer:
	def __init__(sefl, func):
		self.calls = 0
		self.func = func
	def __call__(self, *args, **kwargs):
		self.calls += 1
		print(self.calls)
		return self.func(*args, **kwargs)
	def __get__(self, instance, owner):
		return wrapper(self, instance)
class wrapper:
	def __init__(self, desc, subj):
		self.desc = desc
		self.subj = subj
	def __call__(self, *args, **kwargs):
		return self.desc(self.subj, *args, **kwargs)
```


# Inne zastosowania

Dekoratory:

- Routing we frameworkach webowych
- Mierzenie czasu wykonania
- Systemy ORM
- Systemy bazodanowe
- Wzorce projektowe (np. singleton)
- Atrybuty prywatne
- Sprawdzanie zakresów argumentów
- Testy
