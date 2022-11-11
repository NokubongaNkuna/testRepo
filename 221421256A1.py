#Problem 1
s = 'fullstackslp'

print(s[0])
print(s[11])
print(s[4:9])
print(s[9:])
print(s[7:10])

#Problem 2
reversedString = '' .join(reversed(s))
print(reversedString)

l = [3,7,[5,[1,4,'hello']]]
l[2][1][2] = 'goodbye'
print(l[2][1][2])

#Problem 3
d1 = {'simple_key':'hello'}

print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}

print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d3['k1'][0]['nest_key'][1])

#Problem 4

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
new = set(mylist)
print(new)

#Problem 5

age = 45
name = "Kyle"

"Hello my dog's name is Kyle and he looks 45 years old"
print( "Hello my dog's name is {} and he looks {} years old " .format(name,age))
