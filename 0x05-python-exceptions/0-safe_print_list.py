#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
        except IndexError:
            continue
        count += 1
    print()
    return count
