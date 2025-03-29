# Numbers
x = 1
print (x) # This will print the value of 'x' varible
type (x) # This will print the most updated data type 'x'
print(type(x))
print("\n")

x = x + 1.11
print(x)
print(type(x))
print("\n")

"""     
Indentation Errornum = 8
    num_sq = num ** 2
print(num_sq)
"""

#Multiple Assignment
a,b = 1,2
a,b = b,a+b
print('a =',a)
print('b =',b)
print("\n")

a,b =1,2
a = b
b = a + b
print('a = ',a)
print('b = ',b)
print("\n")

#Formatting Numbers using 'format'
#First parameter: Location for placement
#Second parameter: # of characters
#Third parameter: # of decimal places

# To print in a format way
a = 1
b = 2
print("{} + {} = {}".format(a,b,a+b))

#To format the decimal places
a=1.222
b=2.333
print("{:0.1f} + {:0.1f} = {:0.1f}".format(a,b,a+b))

#To arrange the location
a = 1.222
b = 2.333
print("{1:0.1f} + {0:0.1f} = {2:0.1f}".format(a,b,a+b))
print("\n")
