# coding=utf-8
"""
Moduł udostepniający klasy Person oraz Manager.
"""

from classtools import AttrDisplay


class Person(AttrDisplay):
    """
    Klasa osoby, udostepniająca pola i metody związane z podstawowymi informacjami.
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        """
        Get last name of a Person.

        Returns: last name (str).
        """
        return self.name.split()[-1]
 
    def give_raise(self, percent):
        """
        Increase pay of a Person by given percent.
        
        Args:
            percent: raise scale (double).        
        """
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    """
    Klasa managera dostosowywująca klasę osoby do własnych potrzeb.
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)

    def give_raise(self, percent, bonus=0.10):
        """
        Increase pay of a Manager by given percent adjusted with bonus.

        Args:
            percent: raise scale (double).
            bonus: bonus scale (double).
        """
        Person.give_raise(self, percent + bonus)
 
 
if __name__ == '__main__':
    bob = Person('Robert Czerwony')
    anna = Person('Anna Zielona', job='programista', pay=100000)
    print(bob)
    print(anna)
    print(bob.last_name(), anna.last_name())

    anna.give_raise(0.10)
    print(anna)
    tom = Manager('Tomasz Czarny', 50000)
    tom.give_raise(0.10)
    print(tom.last_name())
    print(tom)
