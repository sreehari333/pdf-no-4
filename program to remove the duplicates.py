my_list = [1, 2, 3, 1, 2, 4, 5, 4, 6, 2]
print("list before", my_list)
temp_list = []

for i in my_list:
    if i not in temp_list:
        temp_list.append(i)

my_list = temp_list

print("list after removig duplicates", my_list)