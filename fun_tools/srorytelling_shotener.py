import textwrap

#open lorem ipsum document for reading to shorten
with open('d:/Dev_Main/Dev_Python/fun_tools/lorem_ipsum.txt') as text_block1:
    w = text_block1.read()
    
    print(textwrap.shorten(w, width=50))
    print(textwrap.shorten(w, width=15))

