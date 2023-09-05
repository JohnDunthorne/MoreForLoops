for x in range(1, 4):
    for y in range(1, 3):
        print(f"({x}, {y})")
print("-" * 30)
numbers = [5, 2, 5, 2, 2]
for x in list(numbers):
    print(x * "x")
print("-" * 30)
numbers2 = [1, 1, 1, 1, 1, 6]
for x_count in numbers2:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)
print("-" * 30)



