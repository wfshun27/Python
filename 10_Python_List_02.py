#Example of Tuple

#Empty Tuple
new_tup=() 
print(new_tup)

#A tuple of integers
new_tup=(10,20,30,40)
print(new_tup)

#A tuple of mixed data type
new_tup=(10,20.2,'thirty',40)
print(new_tup)

#A nested people
new_tup=((10,20,30),(10.1,20.2,30.3),("team","twenty","thrity"))
print(new_tup)

new_tup=(10,(20.2,("thirty",(40))))
print(new_tup)

#Slicing Tuple 
a = ['equity','liability','asset','expense','income']
print(a[0])

a = ['equity','liability','asset','expense','income']
print(a[1])

a = ['equity','liability','asset','expense','income']
print(a[-1])

a = ['equity','liability','asset','expense','income']
print(a[0:2])

#Tuple vs List
b = ['equity','liability','asset','expense','income']
b.append('budget')
print(f"The list is {b}.")
c = ['equity','liability','asset','expense','income']
c.append('budget')
print(f"The list is {c}.")

t = ('equity', 'liability',['asset','expense','income'])
t[2].append('budget') 
print(t)