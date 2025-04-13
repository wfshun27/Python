a, b = 0, 1
list_a=[]
list_b=[]

while a <= 144:
    list_a.append(a)
    a, b = b, a + b
    list_b.append(b)
print(list_a)
print(list_b)

# generate fibonacci sequence
##Shorter version
 
n = int(input("Enter a number: "))

fib = [0, 1]
while fib[-1] + fib[-2] <= n:
    fib.append(fib[-1] + fib[-2])
print(fib)


n1, n2 = 0, 1
count = 0

# Get the number of terms from the user
nfb1 = int(input("How many terms? "))

# check if the number of terms is valid
if nfb1 <= 0:
   print("Please enter a positive integer")

# if there is only one term, return n1

elif nfb1 == 1:
   print("Fibonacci sequence upto",nfb1,":")
   print(n1)

# generate fibonacci sequence

else:

   print("Fibonacci sequence:")
   while count < nfb1:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1