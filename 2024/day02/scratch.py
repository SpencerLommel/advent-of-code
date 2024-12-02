
# This function determines if a list is monotonic or where all numbers are increasing
def is_monotonic_and_in_range(lst):
    char_list = lst
    lst = []
    for i in char_list:
        lst.append(int(i))

    x, y = [], []
    x.extend(lst)
    y.extend(lst)
    x.sort()
    y.sort(reverse=True)
    if(x == lst or y == lst):
        
        for i in range(len(x) -1):
            difference = x[i+1] - x[i]
            if (difference > 3 or difference < 1):
                return False
        return True
    return False

numbers = [90, 91, 93, 96, 100]

print(is_monotonic(numbers))