numbers=[1,2,3,4,5]
squares_list = [num ** 2 for num in numbers]
print("List comprehension:", squares_list)

# Generator expression
squares_generator = (num ** 2 for num in numbers)

print("Generator expression values:")
for square in squares_generator:
    print(square, end=" ")