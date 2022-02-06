import textwrap

with open('d:/Dev_ChL/fun_tools/lorem_ipsum.txt') as text_block1:

    textwrap.shorten(text_block1, width=50)
    textwrap.shorten(text_block1, width=15)

# File "C:\Users\User\AppData\Local\Programs\Python\Python37\lib\textwrap.py", line 406, in shorten
# return w.fill(' '.join(text.strip().split()))
# AttributeError: '_io.TextIOWrapper' object has no attribute 'strip'