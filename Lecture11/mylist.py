class MyList(list):
        def __getitem__(self, offset):
                print(f"Indeksowanie {self} na pozycji {offset}")
                return list.__getitem__(self, offset - 1)
ml = MyList()
ml.append(12)
ml.append(13)
print(ml[1])
