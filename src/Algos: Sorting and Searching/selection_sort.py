import random

random_numbers = [random.randint(1,20) for i in range(10)]
# print(random_numbers)

def selection_sort(values):
    sorted_list = []
    print(values)
    for i in range(len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
        print(values, "              ", sorted_list)
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index

print(selection_sort(random_numbers))