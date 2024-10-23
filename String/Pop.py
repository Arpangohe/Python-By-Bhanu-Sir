#pop(), popitem(), ---> return
# clear

#  Creates a dictionary named data with names as keys and ages as values.
data = {'Arpan' : 23, 'Jalaj': 22, 'Sajal': 2, 'Shivansh': 58}
# print(data.pop('Arpan'))  # Output: 23
print(data) #Prints the entire data dictionary.
value = data.pop('Jalaj')  #Removes the key 'Jalaj' from the dictionary and stores its value (22) in the variable value.
print(data)
print(value) #Prints the value (22) that was associated with 'Jalaj'.
# Creating a new dictionary named datas with names as keys and ages as values, including a nested dictionary for 'none'.
datas = {'Arpan' : 23, 'Jalaj': 22, 'Sajal': 2, 'Shivansh': 58 ,
         'none':{'1':23,'2':54, '3':24}}
# Printing the entire datas dictionary to see its structure and content.
print(datas)
# Removing the key '3' from the nested dictionary under 'none' and storing its value (24) in the variable value.
value = datas['none'].pop('3')
# Printing the value (24) that was associated with '3' in the nested dictionary.
print(value)
# Printing the datas dictionary again to see the changes after removing '3' from the nested dictionary.
print(datas)

# Checking the type of the value associated with the key 'Arpan' in the original data dictionary.
print(type(data['Arpan']))
# Printing the original data dictionary to see its current state.
print(data)
# Removing an arbitrary key-value pair from the original data dictionary and returning it.
data.popitem()
