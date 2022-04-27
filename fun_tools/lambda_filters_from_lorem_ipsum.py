import string
from functools import reduce

#open lorem ipsum document for reading word by word as a list
with open('d:/Dev_Main/Dev_Python/fun_tools/lorem_ipsum.txt') as text_block1:
    dicty = text_block1.read()
    dictara = dicty.split(' ')
    
    #filter out items with "i" in it
    lamba = list(filter( lambda stringa: "i" in stringa, dictara ))

print (lamba)

nums = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x%2==0, nums)
print(list(even))

prod = reduce(lambda x,y: x*y, nums)
print(prod)