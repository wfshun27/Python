x = [0,1,2]
x.insert(0, 1)
print(x)
del x[1]
print(x)
print(sum(x))

list1 = [1,3]
list2 = list1
print(list2)
list1[0] = 4
print(list1)
print(list2)

print(list('hello')) 

nums = [1, 2, 3]
vals = nums
del vals[1:2]
print(vals)  # Output: [1, 3]


d = {}
d[1] = 1 # value of the key integer 1 is integer 1
d['1'] = 2 # value of the key string '1' is 2
d[1] +=1 # update the value of the key integer 1 to 1+1 =2  final list is {1: 2, '1': 2}

sum = 0
for k in d:
    sum += d[k] # sum the values that associate to all the keys >> the answer is 2+2 = 4 (C)
print(sum)
print(d)