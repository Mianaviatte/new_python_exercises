from functools import reduce


def f(a, x):
    return a.x + x

class Obj:
    def f(self, x):
        self.x = x
        return x + 2

obj = Obj()
print(obj.f(2))
print(f(obj, obj.f(2)))


nums = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x%2==0, nums)
print(list(even))

prod = reduce(lambda x,y: x*y, nums)
print(prod)