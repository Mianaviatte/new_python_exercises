listy = []

listy.append (98)
listy.append (2)
listy.append (5)
listy.append ([89, 16, 32])
listy.append (3)
listy.append (4)

#list are count starting with 0,1,2,3...

print (listy[3][0])

#label for index can be value of item in the list

print (listy[listy[1]])

#pleasant wish for you

listy = listy + ['a life', 'love', 'live', 13, 72, 'try to', 'full of', 17, 80, 'sky']
print (listy[11], listy[8], listy[6], listy[12], listy[7])

print (listy[0])

#cheking for items in the list

if 5 in listy:
    print ("you're winning!")

if 'love' in listy:
    print ('love always finds a way!')

#count the lenth of the list before and after deliting an item

print ('there are ' + str(len(listy)) + ' items in the list')
listy.remove (17)
print ('there are ' + str(len(listy)) + ' items in the list without 17')

#have only pair numbers by checking modulo with %

i = 41

while i<46:
    i+=1
    if (i%2)!=0:
        continue
    print ("it's nice to have " + str(int(2*i/3)) + " pies!")
    print ("it's fucked up", i, "pies and", i/2, "muffins")