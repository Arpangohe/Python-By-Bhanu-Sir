lis1=[12,3,44, 'Arpan', 56, 7, 88, 'Jalaj', 33, 4, 5]

print(lis1)

a = lis1[3 : 8 :1]
print(a)
# The line 'b = list[3:8:1]' is incorrect as it is trying to slice a non-existent list 'list'. It should be corrected to slice the actual list 'lis1'.
# Corrected line: b = lis1[3:8:1]
b = lis1[3:8:1]
print(b)

# Slicing is used to extract a subset of elements from a list. Here, we are slicing the list 'lis1' to get two subsets.
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

# The following lines of code are slicing the list 'lis1' in reverse order to extract subsets of elements.
# The slice 'lis1[7:2:-1]' starts from index 7, moves backwards to index 2 (exclusive), and steps backwards by 1 element each time.
# The slice 'lis1[-4:-9:-1]' starts from index -4 (which is equivalent to the 8th element from the end), moves backwards to index -9 (which is equivalent to the 3rd element from the end), and steps backwards by 1 element each time.
# The resulting subsets are then printed.

f = lis1[7 : 2 : -1]
print(f)

g = lis1[-4 : -9 :-1]
print(g)

# This section of the code is designed to print all the elements of the list 'lis1' in reverse order.
# The slice 'lis1[::-1]' starts from the end of the list, moves backwards to the beginning, and steps backwards by 1 element each time.
# The resulting reversed list is then printed.
reversed_lis1 = lis1[::-1]
print(reversed_lis1)

#Practice 

st = "we are here to learn python. and slicing is very helpful"
print(st[7:21])  # prints "here to learn"
print(st[33:])  # prints "slicing is very helpful"
print(st[3:4]+st[12:13]+st[15:16]+st[18:19])  # prints "atlr"
print(st[3:4]+' '+st[12:13]+st[15:16]+st[18:19])  # prints " a tlr"
print(st[3:19:3]) # print "a rtlr"
print(st[0:21]+ st[36:37]+st[21:22]+st[21:22]+st[27:])
print(st[:21] + "Cpp"+ st[27:])