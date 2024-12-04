# 02 Dec 2024
# Spencer Lommel
# D2;Q1 | Merry Christmas :--) 

safe_reports = 0

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

with open("input.txt", "r") as file:
    for line in file:
        numbers = line.split()
        if is_monotonic_and_in_range(numbers):
            safe_reports += 1
    print(f'There are {safe_reports} safe reports!')

        
        
