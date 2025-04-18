"""
if=Elif
In Python, the syntax for an 'if' conditional statement is as follows:
"""
print("\n")
stock_price_ABC = 301
if (stock_price_ABC < 300):
    print("We will buy 500 shares of ABC\n")
elif (stock_price_ABC == 300):
    print("WE will buy 200 shares of ABC\n")
elif (stock_price_ABC > 300):
    print("We will buy 150 shares of ABC\n")

#if=Elif
#If you change the value of the variable
stock_price_ABC = 200
if (stock_price_ABC > 250):
    print("We will sell the stock and book the profit\n")
else:
    print("We will sell keep the stock\n")

"""
Activity: Conditional
"""
income = input("What is your income:")
income = int(income)
if (income > 8000):
    print("High Income")
elif (income > 4000 and income < 8000):
    print("Medium High Income\n")
elif (income > 2000 and income < 4000):
    print("Medium Income\n")
elif (income > 1000 and income < 2000):
    print("Medium Low Income\n")
else:
    print("Low Income\n")

"""
Ternary Operator
"""
order=200
discount=25
if (order >100):
    print(order*discount/100,"\n"
          )
else:
    print("0\n")

"""
While Loop
The while constuct consists of a condition and block of code.
The general syntax for a 'while' loop is as follow:-

while condition/expression:
    block of statements

To begin, the condition is evaluted.
If the condition is true, the 'block  of statements 
Every time, the condition is checked before executing the block of statements
This keeps on reporting until the condition becomes false, it comes out of the loop to exexute the other statements.
"""
#While Loop Example

a = 0 #Varible
while a <= 10:
    a = a + 1
    print(a)

print("We are now out of the loop\n")

"""
Fibonacci and Golden Ratio in Nature
Fibonacci and Golden Ratio in Art and Architure
Golden Ration in Technical Analysis
"""
"""
Activity: Compute Fibonacci Seq and Golden Ratio Using While Loop
Fibonacci nymber is the sum of the previous 2 fibonacci numbers.
1,1,2,3,5,8,21,34,...

Use the while loop to 
* compute the fibonacci sequence up to 144 and 
* compute the golden ratio which is the ration of two subsequent Fibonacci numbers
"""
a, b = 0, 1
count = 0

while count < 13:
    print(a)
    a, b = b, a + b
    count += 1


# first two terms

n1, n2 = 0, 1
count = 0

# Get the number of terms from the user
nterms = int(input("How many terms? "))

# check if the number of terms is valid

if nterms <= 0:
   print("Please enter a positive integer")

# if there is only one term, return n1

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

# generate fibonacci sequence

else:

   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


#Multiple Assignments
a,b=0,1
fib=[]
golden_ratio=[]
while (b<100):
    a=b
    b=a+b
    fib.append(b)
    golden_ratio.append(round(b/a,3))
print(fib)
print(golden_ratio)
