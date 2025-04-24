#Formatting Using String Literals
#Add a "f" before the string quote

#To print in a formatted way
a = 1
b = 2
print(f"{a} + {b} = {a+b} \n")

#To format the decimal places
a = 1.222
b = 2.333
#print("{1:0.1f} + {0:0.1f} = {2:0.1f} \n".format(a,b,a+b))
print(f"{a:0.1f} + {b:0.1f} = {a + b:0.1f} \n")

#To arrange the location
a = 1.222
b = 2.333
print(f"{b:0.1f} + {a:0.1f} = {a+b:0.1f} \n")

"""
Activity: Format Numbers
Use string literals method to format the output as shown below
5.55 + 6.67 + 4.4 = 17
"""
a = 4.444
b = 5.555
c = 6.666
d = a + b + c
print(f"{a:0.2f} + {b:0.2f} + {c:0.2f} = {d:0.0f} \n")

print("{} + {} + {} = {} \n".format(a,b,c,a+b+c))
print("{1:0.2f} + {2:0.2f} + {0:0.1f} = {3:0.0f}".format(a,b,c,a+b+c))
print("\n")