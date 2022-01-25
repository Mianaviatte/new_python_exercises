# binary search is phone book divided in two parts
# works ONLY with sorted lists!

nums = [5, 25, 72, 16, 15, 23, 48, 89, 78, 65, 13, 94, 47]

nums.sort()
# OOP sorting

print(nums)

search_for = 15

lower = 0
higher = len(nums) - 1
index = None
# future index for search_for

while (lower<=higher) and (index is None):
    # repeat until profit
    
    mid = (lower + higher) // 2 
    # middle

    if nums[mid] == search_for:
        # found at middle
        index = mid

    else:
        if search_for<nums[mid]:
            # search left
            higher = mid - 1
        
        else:
            # search right
            lower = mid + 1

print('Needed item', search_for, 'is at', index, 'index')




