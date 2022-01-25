# Euclid's algorithm, is an efficient method for computing 
# the greatest common divisor (GCD) of two integers (numbers), 
# the largest number that divides them both without a remainder.

a = 8
b = 6

def gcd(a,b):
    while a!=0 and b!=0:

        if a>b:
            a=a%b

        else:
            b=b%a
    
    return a+b

print('GCD of', a, "and", b, "is", gcd(a,b))

# LCM stands for Least Common Multiplier and is LCM = (a*b)/GCD

print('LCM is', int((a*b)/gcd(a,b)))