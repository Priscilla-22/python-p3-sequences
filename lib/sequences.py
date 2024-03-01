#!/usr/bin/env python3

my_list = [("John", 2), ("Steve", 1), ("Joe", 3)]


def sort_tuple(tuple_value):

    # returns the key you want to sort by
    return tuple_value[1]


my_list.sort(key=sort_tuple)
print(my_list)


original_list = [3, 6, 4, 2, 1, 5]
print(sorted(original_list))


insert_list = ["a", "b", "c", "d", "f"]
insert_list.insert(4, "e")
print(insert_list)

delete_list = ["a", "b", "c", "d", "e", "f", "g"]
del delete_list[0]
print(delete_list)

del delete_list[0:3]
print(delete_list)


# fibonacci function
def print_fibonacci(length):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    print(fibonacci_sequence)


print_fibonacci(9)
