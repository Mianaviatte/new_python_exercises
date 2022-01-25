#selection sorting - finds the lowest number in a list 
# by comparing each next to the lowest for now in a loop

nums = [5,2,7,30,15,6,79,56,13,48]
print ('The list was: ', nums)

for i in range (len(nums)):
    lowest = i
    #we call the first item the lowest one to start comparison

    for j in range(i+1,len(nums)):
        if nums[j]<nums[lowest]:
            lowest = j
            #if something next is lower 
    
    nums[i], nums[lowest] = nums[lowest], nums[i]

print('The list is now: ', nums)