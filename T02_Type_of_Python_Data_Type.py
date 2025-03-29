
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
b = a +b
print('a = ',a)
print('b = ',b)

#Formatting Numbers using 'format'
# To print in a format way
a = 1
b = 2
print("{}+{}={}".format(a,b,a+b))

#To format the decimal places
a=1.222
b=2.333
print("{:0.1f}+{:0.1f}={:0.1f}".format(a,b,a+b))

#To arrange the location
a = 1.222
b = 2.333
print("{1:0.1f}+{0:0.1f}={2:0.1f}".format(a,b,a+b))

#Formatting Using String Literals
#To print in a formatted way
a = 1
b = 2
print(f"{a}+{b}={a+b}")

#To format the decimal places
a = 1.222
b = 2.333
print("{1:0.1f}+{0:0.1f}={2:0.1f}".format(a,b,a+b))

#To arrange the location
a = 1.222
b = 2.333
print(f"{a:0.1f}+{b:0.1f}={a+b:0.1f}")

#Activity: Format Numbers
a = 4.444
b = 5.555
c = 6.666

print("{} + {} + {} = {}".format(a,b,c,a+b+c))
print(f"{b:0.2f} + {c:0.2f} + {a:0.1f} = {a+b+c:0.0f}")

