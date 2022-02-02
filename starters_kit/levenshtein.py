str1 = "Storytelling"
str2 = "Storing"

# Levenshtein No. 1
def dist(a, b):
    
    def rec(i, j):
        if i == 0 or j == 0:
            # if any str has len=0 then difference is len of other str
            return max(i, j)
            
        elif a[i-1] == b[j-1]:
            # if last char are equal than skip them
            return rec(i-1,j-1)

        else:
            # in any other case delete, add or replace of char is a recordered Levenshtein distance
            return 1+min(rec(i, j-1), rec(i-1, j), rec(i-1, j-1))
    
    return rec(len(a), len(b))
        
print("Levenshtein distance is", dist(str1, str2), "characters.")

# Levenshtein No. 2
lev = dist(str1,str2)

bigger = max([len(str1), len(str2)])
prst = ((bigger - lev)/bigger)*100

print ("String No. 1 is {str1}\n String No. 2 is {str2}\n Similarity: {prst}%".format(str1 = str1, str2 = str2, prst = prst))