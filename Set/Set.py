# Define two sets A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Find the union of sets A and B using the union() method
union_set = A.union(B)
print("Union of A and B:", union_set)

# Define a third set C
C = {2, 33, 7}

# Find the union of sets A, B, and C by chaining the union() method
union_set_A_B_C = A.union(B).union(C)
print("Union of A, B, and C:", union_set_A_B_C)

# Find the intersection of sets A, B, and C by chaining the intersection() method
intersection_set_A_B_C = A.intersection(B).intersection(C)
print("Intersection of A, B, and C:", intersection_set_A_B_C)