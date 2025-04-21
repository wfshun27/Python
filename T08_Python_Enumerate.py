"""
Enumerate()
Adds a counter to an iterable and returns it in the form of an enumerate object.
"""
fruits = ["Apple","Banana","Cherry","Durian"]
x = enumerate(fruits)
print(list(x), "\n")

#Us for loop to display the values

a=[]
for i,f in enumerate(fruits):
    a.append((i,f))    
print(a,"\n")

year=['2017','2018','2019']
revenue=[150000,200000,500000]

for i,y in enumerate(year):
    r = revenue[i]
    print(f"{y}'s revenue is ${r}")

