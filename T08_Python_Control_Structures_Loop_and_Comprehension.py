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
stock_price_ABC = 301
if (stock_price_ABC > 250):
    print("We will sell the stock and book the profit\n")
else:
    print("We will sell keep the stock\n")

#While Loop Example

a = 0 #Varible
while a <= 10:
    a = a + 1.2
    print(a)

print("We are now out of the loop")

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

#For Loop
a=[3,4,5]
for i in a:
    print(i)

fruits=['apple','banana','cherry']
for fruit in reversed(fruits):
    print(fruit)

#Closing prices of the ABC stock over 10 days
Close_Price_ABC = [300,305,287,298,335,300,197,300,295,310] 

for i in Close_Price_ABC:
    if i < 300:
        print("We Buy")
    if i == 300:
        print("No new positions")
    if i > 300:
        print("We Sell")
print("We are now out of the loop") 

#Range
a=range(2,12,2)
print(list(a))

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

for x in range(1,11):
    a = x**2
    print(a)

a = [x**2 for x in range(1,11)]
print(a)

a=[]
for x in range(1,11):
    a.append(x**2)
print(a)
  
#Enumerate()
fruits = ["Apple","Banana","Cherry","Durian"]
x = enumerate(fruits)
print(list(x))

a=[]
for i,f in enumerate(fruits):
    a.append((i,f))    
print(a)

year=['2017','2018','2019']
revenue=[150000,200000,500000]


for i,y in enumerate(year):
    r = revenue[i]
    print(f"{y}'s revenue is ${r}")

#ZIP
names = ['Alfred','Ally','Belinda']
heights = [170,160,155]
c = list(zip(names,heights))
print(c)
print("\n")
for name, height in zip (names, heights):
    a.append((name,height))
print(a)

years=['2017','2018','2019']
revenues=[15000,200000,500000]

data=zip(years,revenues)
for y,r in data:
    print(f"{y}'s revenue is ${r}")

#####################################################

years=['2017','2018','2019']
revenues=[15000,200000,500000]
expense=[90000,100000,250000]

data=zip(years,revenues,expense)
for y,r,e in data:
    print(f"{y}'s revenue is ${r} and expense is ${e}")

#Break
for i in range(10):
    if i==4:break
    print(i)

#List Comprehension
d = [i*i for i in range(1,11)]
print(d)

d = [i*i for i in range(1,11) if i%2==0]
print(d)

for x in range(1,11):
    print(x)
    a = x*x
    print(a)

#Dict Comprehension
d = {i:i*i for i in range(1,11)}
print(d)

#Example
d = {i:i**2 for i in range(1,19) if i%3!=0 and i%5!=0}
print(d)


a=[1,2]
b=[3,4]
for d, c in zip (b, a):
    a.append((d,c))
print(a)