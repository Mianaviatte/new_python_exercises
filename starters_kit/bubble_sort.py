# bubble sorting:
# each of numbers is compared to all the rest, moving by list index 
# 00 01 02 03... 12 13 14... 23 24 25 ... 34 35 36... 45 46 47...
# until the end of a list

numbers = [2,5,6,4,9,8,3,1,7]

for i in range(len(numbers)):
        for j in range(len(numbers) -i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print (numbers)

newnumbers = [12,15,16,14,19,18,13,11,17]

swaps = True
while swaps:
    swaps = False

    for j in range(len(numbers)-1):
        if newnumbers[j] > newnumbers[j+1]:
            swaps = True
            newnumbers[j], newnumbers[j+1] = newnumbers[j+1], newnumbers[j]

print (newnumbers)