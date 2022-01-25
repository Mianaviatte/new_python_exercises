#factorial is the product of an integer and all the integers below it. 
# e.g. factorial four ( 4! ) is equal to 24.

number = int(input ('set a number '))

def factorial(n):
    if n==0:
        return 1

    f=1
    i=0

    while i<n:
        i+=1
        f=f*i
    
    return f

print('Factorial of {n} equals {f}'.format(n=number, f=factorial(number)))
