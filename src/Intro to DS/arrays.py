new_list = [1, 2, 3]
result = new_list[0]

if 1 in new_list:
    print(True)

for n in new_list:
    if n == 1:
        print(True)
        break

numbers = []
print(len(numbers))
numbers.append(2)
numbers.append(200)
print(numbers)

"""
For accessing the values, it is constant time O(1),
but appending or removing takes linear time O(n).
"""