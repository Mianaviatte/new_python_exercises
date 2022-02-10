k=0

def f():
    global k
    k+=1
    return f

# few times () is one more time done!
f()()()()()
print(k)   #5

n = 13,17,15,2
n = str(n)
n = n.replace('(', '')
n = n.replace(')', '')
n = n.split(',')

# how to convert str to int in list?
n.insert(2, 14)
n.insert(3, 16)  #will not work if it's tuple! if list then works!
print(n)

txt = "The best things in life are free!"
print("free" in txt)

l = [12, 17, 32, 67, 34, 89, 96, 2]
r = -1
m = l[2:r]
print(m, "if end parameter is", r)

index_of_max = max((item, i) for i, item in enumerate(l))[1]
print('Index of max item in list L:', index_of_max)


z =(int(input('Tell me any number: ')))
c = True if z**3>100 else False
print(c)

print(bool("Hello")) #True
print(bool(15)) #True

arr = [0, 1, 2, 3, 4]
y = arr[len(arr)-1]
if not y%4:
    print(len(arr))
    print(y)
    print(y%4)
else:
    print(arr[y])
