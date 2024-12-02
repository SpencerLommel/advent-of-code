# Testing file

# Make function that takes list and returns dict of value and num of occurences

nums = [1, 2, 3, 3, 4, 8, 2]
frequency_dictionary = {}

# print(3 in frequency_dictionary)
# print(frequency_dictionary[1])

# if 1 in frequency_dictionary:
#     frequency_dictionary[1] += 1

# print(frequency_dictionary[1])

for n in nums:
    if n in frequency_dictionary:
        frequency_dictionary[n] += 1
    else:
        frequency_dictionary[n] = 1

print(frequency_dictionary)


