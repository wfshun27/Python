# To print in a format way
a = 1
b = 2
print("{} + {} = {}".format(a,b,a+b), "\n")

#To format the decimal places
a=1.222
b=2.333
print("{:0.1f} + {:0.1f} = {:0.1f}".format(a,b,a+b),"\n")

#To arrange the location
a = 1.222
b = 2.333
print("{1:0.1f} + {0:0.1f} = {2:0.1f}".format(a,b,a+b), "\n")
