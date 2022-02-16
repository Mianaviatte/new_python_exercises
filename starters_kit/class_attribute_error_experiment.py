class NotSafeOne:
    def __init__(self, attrybute1):
        self.attribute1 = attrybute1


a = NotSafeOne("Everybody can access")
print(a.attribute1)


class SafeSecond:
    def __init__(self, attribute2):
        self.__attribute2 = attribute2


b = SafeSecond("Nobody should access")

try:
    print(b.__attribute2)
except AttributeError:
    print("Sorry, access denied!")
finally:
    print(b._SafeSecond__attribute2)
