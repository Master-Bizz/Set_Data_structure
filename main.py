print("Hello William") 
def greet (name):
 return f"Welcome back.. {name}"
print(greet('William'))
quad = []
for x in range(10):
   quad.append(x**4)
   print(quad)
print(quad[2:11])
print(quad[-5:])
print(quad[-5])
#==================================================
# Set items are enclosed in curly brackets
# Set is unordered
# Set is mutable, can contain only immutable items
# Set elements are unique
# Elements can contain only immutable items

"""
Sets can be used for mathematical set operations such as union, intersection, difference 
and symmetric difference.

https://en.wikipedia.org/wiki/Set_(mathematics)
"""

"""
Python Set Attributes
"""

print(dir(set))

"""
Creating Python Sets
"""
#  set = set()
# set = {1,2,3,4}
# print(set)


"""
Modifying a set in Python
"""
set_example = {'Hello', 'people'}
set_example.add('Yoo')
set_example.update([12,21,45])
print(set_example)

print(help(set.update))

"""
Removing elements from a set
"""
set_example2 = {1,12,23,4}
set_example2.discard(1)
print(set_example2)
set_example2.remove(4)
set_example2.add(8)
set_example2.update({5})
print(set_example2)
set_example.pop()
print(set_example2)

print({"boom", "boom", "k", "k"})  # leaves out duplicates

"""
Set Union Operations 
"""
# adds sets together
a = {1,2,3,4}
b = {7,8,9}
print(a | b)     
print(a.union(b))   # same thing, but another way using 'Union'!

"""
Set Intersection Operations 
"""
# Finds the mode of both sets
c = {11,21,31,14}
d = {71,81,91,21,31}
print(c & d)     
print(c.intersection(d))  # Same again now using intersection

"""
Set Difference Operations
"""
# finds things that dont exist in the next set from the reference set.
e = {32,30,33,34, 39}
f = {34,32,33,33}
print(e - f)     
print(e.difference(f))
print(help(set.difference)) # ""

"""
Set Symmetric Difference
"""
# Combines elements not in the reference set and vice versa
g = {32,30,33,34,39}
h = {34,32,33,36,37}
print(g ^ h)
print(g.symmetric_difference(h)) # ""

"""
Set Methods
"""

print(dir(set))








# add() - Adds an element to the set
# clear() - Removes all the elements from the set
# copy() - Returns a copy of the set
# difference() - Returns a set containing the difference between sets
# difference_update() - Removes the items in this set that are also in another
# discard() - Remove the specified item
# intersection() - Returns a set, that is the intersection of two other sets
# intersection_update() - Removes items in a set that are not present in other
# isdisjoint() - Returns whether two sets have a intersection or not
# issubset() - Returns whether another set contains this set or not
# issuperset() - Returns whether this set contains another set or not
# pop() - Removes an element from the set
# remove() - Removes the specified element
# symmetric_difference() - Returns a set with the symmetric differences
# symmetric_difference_update() - inserts the symmetric differences
# union() - Return a set containing the union of sets
# update() - Update the set with the union of this set and others