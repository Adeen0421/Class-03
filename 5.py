\
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):  
    fruits[i] = "Yummy " + fruits[i].upper()  

for fruit in fruits:  
    print(fruit)


    word: str = "Programming"
for letter in word:
    print(letter)


    numbers = [3, 7, 11, 20, 5]

for num in numbers:
    print(num)
else:
    print("Loop completed successfully!")

    numbers = [12, 23, 32, 54, 59]

for num in numbers:
    print(num)
    if num == 54:
        print("Breaking the loop!")
        break
else:
    print("Loop completed successfully!") 


for _ in range(15):
     print(f"Hello, World! Iteration { _ }")

     # Print numbers from 1 to 5
count: int = 1
while count <= 7:
    print(count)
    count += 1


for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4


    # Multiplication table
for outer in range(1, 6): # outer loop
    print(f"Multiplication table for {outer}:")
    for inner in range(1, 6): # nested inner loop
        print(f"{outer} * {inner} = {outer * inner}")
    print()  # Add a blank line after each row

    n = 100
total = (n * (n + 1)) // 2  # Using integer division
print("Sum of numbers from 1 to 100:", total)


# Find factors of a number
num: int = 226
factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
print(f"Factors of {num}: {factors}")