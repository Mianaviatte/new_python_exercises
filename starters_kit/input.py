x=13
y=7
i=5

#to try commenting


while i>=1:
	print (i)
	i=i-1

print ("""
Hi there!
Here are my numbers: """)
print (x, y)

while True:
	try:
	  x=input ('''
Set your first number: ''')
	 
	  x=int(x)
	  y=int(input ('Set your second number: '))
	  print("That's the lucky numbers!", )
	  
	except ValueError:
	    print("Something went wrong")

	
	if y!=10 and (x<10 or x>=40):

		print ('multiplied: ', x*y)
		print ('is x 20? ', x==20)
		print ('is y equal or less than 10? ', y<=10)
		print ('is y equal or more than 10? ', y>=10)

	elif y==10 and not x>=40:
		print ('is x equal or less than 20? ', x<=20)
		print ('is x equal or more than 21? ', x>=21)	  
		
		while x<38:
			x+=2
			print ('we scale x by two, now x equals ', str(x))
			print ('multiplied: ', x*y)

	else:
			x+=7
			y+=3
			print ('we scale x by seven and y by three')
			print ('multiplied: ', x*y)
			print ('is x 15? ', x==15)
			print ('is y equal or more than 14? ', y>=14)

print('Profit!')