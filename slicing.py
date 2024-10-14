lis1=[12,3,44, 'Arpan', 56, 7, 88, 'Jalaj', 33, 4, 5]

print(lis1)

a = lis1[3 : 8 :1]
print(a)
b = list[3:8:1]
print(b)

# Slicing is used to extract a subset of elements from a list. Here, we are slicing the list 'lis1' to get two subsets.
# 'c' is assigned the slice of 'lis1' from index 3 to 6 (exclusive), which includes elements at indices 3, 4, and 5.
# 'd' is assigned the slice of 'lis1' from index 8 to the end of the list, which includes all elements starting from index 8.
# The '+' operator is used to concatenate the two lists 'c' and 'd', effectively combining the two subsets into a single list.
# The resulting combined list is then printed.
c = lis1[3 : 6]
d = lis1[8:]
print(c+d)

# This section of the code is combining two slices of the list 'lis1' into a single list 'e'.
# The first slice 'lis1[3:6]' includes elements at indices 3, 4, and 5.
# The second slice 'lis1[8:]' includes all elements starting from index 8 to the end of the list.
# The '+' operator is used to concatenate these two slices, effectively combining them into a single list 'e'.
# Finally, the combined list 'e' is printed.
e = lis1[3:6]+lis1[8 :]
print(e)

