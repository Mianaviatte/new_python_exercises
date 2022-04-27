from ast import comprehension


#comprehension to create set of int values
x = set([i*j for i in range(10) for j in range(10) if i%2==0 and (i*j)!=0])
print(x)

#comprehention to count letters in sentence and save as dictionary
sentence = "Try my tasty donnuts for breakfast tomorrow."
y = {char: sentence.count(char) for char in sentence}
print(y)


#list slice
l = [12, 17, 32, 67, 34, 89, 96, 2]
r = -1
m = l[2:r]
print(m, "if end parameter is", r)
#comprehention to find index of max item in list 
index_of_max = max((item, i) for i, item in enumerate(l))[1]
print('Index of max item in list L:', index_of_max)