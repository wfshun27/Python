#List
# Empty List
new_list = []
print(type(new_list))
print(new_list)
print("\n")

#A List of integers
new_list = [10, 20, 30, 40]
print(type(new_list))
print(new_list)
print("\n")

#A List of mixed data types
new_list = [[10, 20, 30, 40], ["ten", "twenty", "thirty"]]
print(new_list)
print(type(new_list))
print("\n")

#A Nested List
new_list = [[10, 20, 30], [10.1, 20.2, 30.3], ["ten", "twenty", "thirty"]]
print(new_list)
print(type(new_list))
print("\n")

#A Deeply Nested List
new_list = [10, [20.2, ["thirty", [40]]]]
print(new_list)
print(type(new_list))
print("\n")

# Slicing List
a = [7,8,9,10,11]
print(a[0])
print(a[2])
print(a[0:3]) #Position 0 to 3
print(a[2:4]) #Position 2 to 4
print(a[-1])  #Backward
print(a[-2])
print(a[:])
print(a[0:4:2]) #Position to 4 take 2 Steps
print("\n")

#Index
a = ['equity', 'liability', 'asset', 'expense', 'income']
print(a.index('expense'))
print("\n")

#Append
a = ['equity', 'liability', 'asset', 'expense', 'income']
print(a.append('expense'))
print(a, "\n")

#Extend
a = ['equity', 'liability', 'asset', 'expense', 'income']
b = ['cash flow', 'budget']
b.extend(a)
print(b, "\n")

#INSERT
a = ['equity','liability','assest','expense','income']
a.insert(2,'budget')
print(a, "\n")

#REMOVE
a = ['budget','equity','liability','asset','expense','income']
a.remove('budget')
print(a, "\n")

#Pop
a = ['budget','equity','liability','asset','expense','income']
a.pop()
print(a, "\n")


a = ['budget','equity','liability','asset','expense','income']
a.pop(2)
print(a, "\n")

#Count
a = ['budget','equity','liability','asset','expense','income','income']
print(a.count('income'), "\n")

#Reverse
a = ['budget','equity','liability','asset','expense','income']
a.reverse()
print(a, "\n")

#Sort
a = ['budget','equity','liability','asset','expense','income']
a.sort()
print(a)
print("\n")

#Copy list
a = ['equity', 'liability', 'asset', 'expense', 'income']
b = a.copy()
b.pop()
print(a)
print((b), "\n")

#Activity: List
"""
Copy from original years to years 2
Remove 2021 in years 2
Insert '2019' in location 2 in years 2
Reverse the order of years 2
"""
years=['2017', '2018', '2020', '2021']
years2=years.copy()
years2.pop()
print(years2, "\n")
years2.insert(2,2019)
print(years2, "\n")
years2.reverse()
print(years2, "\n")