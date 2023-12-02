# 2 + 2 =5

class MyInt(int):
    def __add__(self, x):
        return super().__add__(x+1)

y = MyInt(2)

