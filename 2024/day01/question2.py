# 02 Dec 2024
# Spencer Lommel
# D1;Q2 | Merry Christmas :--) 

left_column = []
right_column = []
similarity_score = 0
frequency_dictionary = {}

with open("input.txt", "r") as file:
    for line in file:
        numbers = line.split()
        left_column.append(int(numbers[0]))
        right_column.append(int(numbers[1]))


# Sorting is unecessary but keeps the data looking nice for testing :--)
left_column.sort()
right_column.sort()

for n in right_column:
    if n in frequency_dictionary:
        frequency_dictionary[n] += 1
    else:
        frequency_dictionary[n] = 1


for n in left_column:
    if n in frequency_dictionary:
        similarity_score += n * frequency_dictionary[n]

print(similarity_score)

