class Klasa:
    def __init__(self, value):
        self.__val = value
    def __method(self):
        
        print('In __method')
    def other(self):
        self.__method()
        print(dir(self))
        print(self.__dict__)
        
k = Klasa(12)
k.other()
k._Klasa__method()
print(k.__val)