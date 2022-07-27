numbers = [49, 5, 8, 14, 3, 7, 6, 21]

seven_list = []

for i in numbers:
    if i%7 == 0:
        seven_list.append(i)

min_number = min(seven_list)

result = numbers.index(min_number)

print(result)