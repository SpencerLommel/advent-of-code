# 02 Dec 2024
# Spencer Lommel
# D2;Q1 | Merry Christmas :--) 
safe_reports = 0

def is_monotonic_and_in_range_with_tolerance(lst):
    faults = 0
    char_list = lst
    lst = []
    for i in char_list:
        lst.append(int(i))

    direction = "increase" if (lst[0] + lst[1] < lst[-1] + lst[-2]) else "decrease"

    if direction == "increase":
        for i in range(len(lst) - 1):
            difference = lst[i+1] - lst[i]

            if not(difference > 1 and difference < 3):
                faults += 1

    if direction == "decrease":
        for i in range(len(lst) - 1):
            difference = lst[i] - lst[i+1]

            if not(difference > 1 and difference < 3):
                faults += 1

    print(f'{lst} : {direction} : {faults}')
        

                 

    

        





    


with open("input.txt", "r") as file:
    for line in file:
        report = line.split()
        if is_monotonic_and_in_range_with_tolerance(report): safe_reports += 1

    print(f'There are {safe_reports} safe reports!')
