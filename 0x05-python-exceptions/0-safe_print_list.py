#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for e in my_list:
            if e == x:
                break
            print("{}".format(e), end="")
            i += 1
        print("\n", end="")
        return i
    except IndexError:
        print("\n", end="")
        return i
