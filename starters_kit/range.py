#to print each item in a list we count lensy as index to every item and compate with i starting with 0
#if there are 5 items in the list, their indexes will be 0,1,2,3,4. So lensy will be 4 to adress each item. 

rura = list (range(15, 22, 3))

i = 0
lensy = len(rura) - 1

while i <= lensy:
    print (rura[i], "kitties run in my room while there are" )
    i += 1

#or the easy way to do the same thing!!!

for each in rura:
    print ( int( each **7/2), 'stars above us pray for your souls, or prey... who knows?' )