#comprehension to sum values by unified register keys in dictionary
m = {'a': 10, 'k': 23, 'z': 78, 'n': 14, 'K': 56, 'A': 97, 'l': 8, 'R': 19}
m_sum = {k.lower(): m.get(k.lower(),0) + m.get(k.upper(),0) for k in m}
print(f'The new dictionary with unified key\'s register is {m_sum}')

#comprehension to create set of int values
x = {i*j for i in range(10) for j in range(10) if i%2==0 and (i*j)!=0}
print(f'There are unicue multiplies of range(10): {x}')

#comprehention to count letters in sentence and save as dictionary
sentence = "Try my tasty donnuts for breakfast tomorrow."
y = {char: sentence.count(char) for char in sentence}
print(f'In sentence "{sentence}" there are', y)


#list slice
l = [12, 17, 32, 67, 34, 89, 96, 2]
r = -1
f = l[2:r]
print(f'{f} is the sliced list if end parameter is {r}')

#comprehention to find index of max item in the list 
index_of_max = max((item, i) for i, item in enumerate(f))[1]
print('Index of max item in sliced list L:', index_of_max)