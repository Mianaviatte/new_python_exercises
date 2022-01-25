k=0

def f():
    global k
    k+=1
    return f


# few times () is one more time!
f()()()()()
print(k)   #5

a = "Hello, World!"
print(a.lower())
print(a.upper())

n = 13,17,15,2
n = str(n)
n = n.replace('(', '')
n = n.replace(')', '')
n = n.split(',')

# how to convert str to int in list?

n.insert(2, 14)
n.insert(3, 16)  #will not work if it's tuple! if list then works!
print(n)

for x in "banana":
    print(x)

txt = "The best things in life are free!"
print("free" in txt)

l = [12, 17, 32, 67, 34, 89, 96, 2]
r = -1

m = l[2:r]

print(m, "if end parameter is", r)

z=(int(input('Tell me any number: ')))
c= True if z**3>100 else False
print(c)

print(bool("Hello")) #True
print(bool(15)) #True