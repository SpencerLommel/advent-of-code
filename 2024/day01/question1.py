# 02 Dec 2024
# Spencer Lommel
# D1;Q1 | Merry Christmas :--) 

left_column = []
right_column = []
total_distance = 0

with open("input.txt", "r") as file:
    for line in file:
        numbers = line.split()
        left_column.append(int(numbers[0]))
        right_column.append(int(numbers[1]))

left_column.sort()
right_column.sort()

for i in range(0, len(left_column)):
    total_distance += abs(left_column[i] - right_column[i])

print(total_distance)