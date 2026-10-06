numbers=[1,2,3,4,5]
squares_list = [num ** 5 for num in numbers]
print("List comprehension:", squares_list)


squares_generator = (num ** 6 for num in numbers)
print(squares_generator)
print("Generator expression values:")
for square in squares_generator:
    print(square, end=" ")