my_set = {123, 452, 5, 6}
my_set2 = set([123, 452, 5, 6])
unknown = {}
empty_set = set()

print("my_set            = ", my_set)
print("my_set2           = ", my_set2)
print("type(my_set)      = ", type(my_set))
print("type(my_set2)     = ", type(my_set2))
print("type(unknown)     = ", type(unknown))
print("type(empty_set)   = ", type(empty_set))
print("my_set == my_set2 = ", my_set == my_set2)

multi_type_set = {7, 9.0, False, True, "Hello! World", (1, 5, 9, 'hi')}
print(multi_type_set)

set2 = {'Java', 'Python', 'JavaScript', 'java'}
print(set2)

my_set = {1, 2, 3, 4, 5}
print(my_set)

try:
    my_set[0] = 10
except TypeError as e:
    print("*TypeError*  ABC : ", e)

print("Program execution continues as normal because we handle the error condition in try except block")

my_set = {1, 2, 3, 4, 5, 'A', 'a'}
print(my_set)
my_set.remove(3)
my_set.remove('A')
print(my_set)

my_set.add(6)
print(my_set)

print("my_set = ", my_set)
print(my_set.discard({1, 2, 3}))
print("After: my_set = ", my_set)

for item in {1, 2, 3}:
    my_set.discard(item)

print("After removing multiple elements: my_set = ", my_set)

print("Before: my_set = ", my_set)
my_set.difference_update({1, 5, 3, 'A'})
print("After:  my_set = ", my_set)

print("Before: ", my_set)
my_set.update([7, 8, 9, "Hello"])
print(my_set)

my_set = {1, 2, 3, 5}
my_set_2 = {1, 5, 6, 7}
my_set3 = my_set.union(my_set_2)
print(my_set3)

my_set3 = my_set | my_set_2
print(my_set3)

my_set = {1, 2, 3, 4, 5, "Hello! World"}
print("Before : ", my_set)
my_set.add(2)
my_set.add("Hello! World")
print("After  : ", my_set)

my_set = {1, 2, 3}

try:
    my_set.remove(4)
except KeyError as e:
    print("KeyError: ", e)

print("Before pop() = ", my_set)
my_set.pop()
print("Before pop() = ", my_set)

my_set.discard(4)
print(my_set)

a = "Hello! World"
b = "Hello! World"

print("id(a) = ", id(a))
print("id(b) = ", id(b))
print("hash(a) = ", hash(a))
print("hash(b) = ", hash(b))
print("hash(a)      = ", hash(a))
print("a.__hash__() = ", a.__hash__())

my_frozenset = frozenset([1, 2, 3, "Hello! World"])
print("my_frozenset  = ", my_frozenset)

my_frozenset2 = frozenset(my_set)
print("my_frozenset2 = ", my_frozenset2)

my_set = {1, 2, 3, "Hello! World", 4, 5, 6}
my_set2 = {1, 2, 3, "Hello! World", 8, 9}
my_set3 = {1, 2, 3, "Hello! World", 77}

print("difference()           = ", my_set.difference(my_set2, my_set3))
print("intersection()         = ", my_set.intersection(my_set2, my_set3))
print("union()                = ", my_set.union(my_set2, my_set3))
print("symmetric_difference() = ", my_set.symmetric_difference(my_set2))
print("isdisjoint()           = ", my_set.isdisjoint(my_set2))
print("issuperset()           = ", my_set.issuperset(my_set2))
print("issubset()             = ", my_set2.issubset(my_set))

import gc
gc.collect()
print(gc.get_count())
