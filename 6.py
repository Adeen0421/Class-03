fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = ["hello", 42, 3.14, True]

print("fruits  = ", fruits)
print("numbers = ", numbers)
print("mixed   = ", mixed)

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-3])

fruits = ["apple", "banana", "cherry"]
fruits[-3] = "watermelon"
print(fruits)

print(fruits[0:2])

fruits.append("mango")
print(fruits)

fruits.extend(["grape", "kiwi"])
print(fruits)

fruits.remove("banana")
print(fruits)

deleted = fruits.pop(1)
print("deleted element = ", deleted)
print(fruits)

numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)

numbers = [4, 2, 9, 1]
numbers.sort(reverse=True)
print(numbers)

words = ["apple", "kiwi", "banana"]
words.sort(key=len)
print(words)

words = ["apple", "kiwi", "banana"]
words.sort(key=lambda word: word[-1])
print(words)

numbers = [1, 2, 5, 7, 10]
numbers.reverse()
print(numbers)

for fruit in fruits:
    print(fruit)

squared = [x**2 for x in [1, 2, 3, 4, 5]]
print(squared, " : ", type(squared))

squared = [x**2 for x in [1, 2, 3, 4, 5] if x > 3]
print(squared, " : ", type(squared))

tuple1 = tuple(["apple", "banana", "cherry"])
tuple2 = (10, 20, 30)
mixed_tuple = ("hello", 42, 3.14, True)

print("tuple1      =", tuple1)
print("tuple2      =", tuple2)
print("mixed_tuple =", mixed_tuple)

tuple_1 = (10, 20, 30)
tuple_2 = (10, 20, 30)

print("id(tuple_1) = ", id(tuple_1))
print("id(tuple_2) = ", id(tuple_2))

print("tuple_1 == tuple_2 = ", tuple_1 == tuple_2)

print("tuple1[0] =", tuple1[0])
print("tuple2[1:] =", tuple2[1:])
print("Length of tuple1:", len(tuple1))

print("Iterating through tuple2:")
for item in tuple2:
  print(item)

print("Is 20 in tuple2?", 20 in tuple2)

tuple3 = tuple1 + tuple2
print("tuple1 + tuple2 =", tuple3)

tuple4 = tuple2 * 2
print("tuple2 * 2 =", tuple4)

nested_tuple = (tuple1, tuple2)
print("nested_tuple =", nested_tuple)

a, b, c = tuple1
print("Unpacking tuple1:", a, b, c)

my_dict = {tuple1: "This is a tuple key", tuple2: "Another tuple key"}
print("Dictionary with tuple keys:", my_dict)

print(tuple1[0])
print(tuple1[-3])
print(tuple1.count("apple"))
print(tuple1.index("apple"))

tuple_methods = [method for method in dir(tuple) if not method.startswith('__')]
tuple_methods

tuple1 = tuple(["apple", "banana", "cherry"])
print(tuple1.count("apple"))
print(tuple1.index("apple"))
example_tuple = ('count', 'index')
print(example_tuple)

a = input("Enter your name: ")
print(a, type(a))

american_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
american_cities

person = {
    "name": "Alice",
    "age": 25,
    "visited_cities": american_cities
}
print(person)

thisdict = dict(name="John", age=36, country="Norway")
print(type(thisdict)," - ", thisdict)

print(person["name"])
print(person.get("age", "99"))
print(person.get("country", "my_default_vlaue_if_key_not_found"))

person["email"] = "alice@example.com"
print(person)

person["age"] = 26
print(person)

person = {'name': 'Alice', 'age': 25, 'email': 'alice@example.com', 'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
print(person)

del person["city"]
print(person)

age = person.pop("age", -1)
print("Removed age:", age)
print(person)

print("\n-----\n")
age = person.pop("age", -1)
print("key 'age' not found in dict so returning default value: ", age)

print("person.keys()         = ", person.keys())
print("person.values()       = ", person.values())
print("person.items()        = ", person.items())

person.update({"city": "Los Angeles", "age": 27})
print("After: person.update  = ", person)

person.clear()
print("After: person.clear() = ", person)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

for key in thisdict:
    print(key)

for key, value in thisdict.items():
    print(key," : ", value)
