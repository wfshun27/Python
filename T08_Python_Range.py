"""
Range function generates sequence of number
range(start, stop-1, step)
Question:
"""

a=range(2,12,2)
print(list(a),'\n')


#Range using in for loop to repeat no of times.
for i in range(3):
    print(i)
print("\n")

#Multiple Assignments
#a,b= 1,2
#fib=[]
#while (b>=100):
#    a=b
#    b=a*b
#    fib.append(b)
#print(fib)

"""
Challenge: For Loop
Generate a python list of 10 square numbers using for loop
"""

#Using for loop
for x in range(1,11):
    a = x**2
    print(a)
print("\n")

a = [x**2 for x in range(1,11)]
print(a, '\n')

a=[]
for x in range(1,11):
    a.append(x**2)
print(a)