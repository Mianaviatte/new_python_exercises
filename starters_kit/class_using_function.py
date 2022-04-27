#class using function on itself

def f(a, x):
    return a.x + x

class Obj:
    def f(self, x):
        self.x = x
        return x + 2

obj = Obj()
print(obj.f(2))
print(f(obj, obj.f(2)))