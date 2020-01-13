class good_int(int):
    def __new__(cls, value):
        if value in {2137, 69}:
            print('Nice!')
        return int.__new__(cls, value)

gi = good_int(12)

print(gi)

gi2 = good_int(69)
gi3 = good_int(2137)


print(gi2 + gi3)



