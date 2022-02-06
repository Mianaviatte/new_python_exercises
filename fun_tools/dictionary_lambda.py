import string


with open('d:/Dev_ChL/fun_tools/lorem_ipsum.txt') as text_block1:
    dictara = text_block1.split(' ')
    # AttributeError: '_io.TextIOWrapper' object has no attribute 'split'

    lamba = list(filter( lambda stringa: "i" in stringa, dictara ))


print (lamba)