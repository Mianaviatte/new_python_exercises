from num2words import num2words

# how to convert int to str in list?
n = 13,17,15,27
n = str(n)
n = n.replace('(', '')
n = n.replace(')', '')
n = n.split(',')
n.insert(2, 14)
n.insert(3, 16)  #will not work if it's tuple! if list then works!
m = [num2words(num, to='ordinal') for num in n]
print(m)