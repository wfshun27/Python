"""
Dictionary is a list of keys. Each key is associated with a value.
Each key is separated from its value by a colon
Dictionary is enclosed by curly braces
"""

#Empty Dictionary
new_dict = []
print(new_dict)
print(type(new_dict), "\n")

#Creating a new dictionary
revenue = {'2017','1.3M','2018','2.2M','2019','3.5M'}
print(revenue)
print(type(revenue), "\n")

#Printing multiple values of various keys
revenue = {'2017':'1.3M','2018': '2.2M','2019':'3.5M'}
print(revenue['2017'], revenue['2019'])
print(type(revenue), "\n")

#LEN
revenue = {'2017':'1.3M','2018': '2.2M','2019':'3.5M'}
print(len(revenue))

#KEYS
revenue = {'2017':'1.3M','2018': '2.2M','2019':'3.5M'}
print(revenue.keys())

#Values
revenue = {'2017':'1.3M','2018': '2.2M','2019':'3.5M'}
print(revenue.values())

#Items
revenue = {'2017':'1.3M','2018': '2.2M','2019':'3.5M'}
print(revenue.items())

#Pop
revenue = {'2017':'1.3M','2018': '2.2M','2019':'3.5M'}
print(revenue.pop('2018'))
print(revenue)

#DEL
revenue = {'2017':'1.3M','2018': '2.2M','2019':'3.5M'}
del revenue['2017']
print(revenue)

#Set
new_set = {'equity', 'liability', 'asset', 'expense','income'}
print(new_set)
type(new_set)

#Now there are 2 'equity' in our set. What will happen if we print this set?
new_set = {'equity', 'liability', 'asset', 'expense','income', 'equity'}
print(new_set)

#Union
a = {'equity','liability','asset'}
b = {'asset','expense','income'}
print(sorted(b.union(a)))

#intersection
a = {'equity','liability','asset'}
b = {'asset','expense','income'}
print(a.intersection(b))

#difference
a = {'equity','liability','asset'}
b = {'asset','expense','income'}
print(a.difference(b))

#subset
a = {'equity', 'liability', 'asset',}
b = {'asset'}
print(b.issubset(a))
print(b <= a)

#Suerset
a = {'equity', 'liability', 'asset'}
b = {'equity', 'liability', 'asset', 'expense', 'income', 'equity'}
print(b.issuperset(a))


sentence = "A budget is quantitiative plan for acquiring and using resources over a specified period."

# Convert sentence to lowercase and split into words
words = sentence.lower().split()
print(words)

# Use a set to store unique words
unique_words = set(words)

# Print the number of unique words and the words themselves
print("Unique Vocabulary Count:", len(unique_words))
print("Unique Words:", unique_words)



