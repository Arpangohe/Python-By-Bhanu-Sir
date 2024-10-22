#pop(), popitem(), ---> return
# clear

#  Creates a dictionary named data with names as keys and ages as values.
data = {'Arpan' : 23, 'Jalaj': 22, 'Sajal': 2, 'Shivansh': 58}
# print(data.pop('Arpan'))  # Output: 23
print(data) #Prints the entire data dictionary.
value = data.pop('Jalaj')  #Removes the key 'Jalaj' from the dictionary and stores its value (22) in the variable value.
print(data)
print(value) #Prints the value (22) that was associated with 'Jalaj'.