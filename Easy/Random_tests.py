list_of_nums = [12, 345, 2, 6, 7896]
total = 0

for i in list_of_nums:
    if len(str(i)) % 2 == 0:
        print(f"List of nums with even digits {i}")

nums = [-4, -1, 0, 3, 10]
sorted_list = []

for i in nums:
    sorted_list.append(abs(i) ** 2)

for i in sorted_list:
    print(f"Sorted list squared:{i}")
