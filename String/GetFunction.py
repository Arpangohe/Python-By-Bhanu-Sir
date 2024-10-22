# get(key) ----> return Value

data = {'Arpan' : 23, 'Jalaj': 22, 'Sajal': 2, 'Shivansh': 58}
a=data['Shivansh']
print(a)

# now use get function

data = {'Arpan' : 23, 'Jalaj': 22, 'Sajal': 2, 'Shivansh': "mistake of God and Parents"}
b=data.get('Shivansh')
print(b)

    # but if we are calling a key who is not availble here is show none here is the example

c=data.get('Ashi')
print(c)     # output is none

# -------------   setdefault()  function ------------- 

datas = {'1': 123, '2': 566, '3': 899}
# setdefault() function is used to set a default value for a key if it is not available
# it returns the value for the given key if it exists in the dictionary. If not, it
value = data.setdefault('11',789)
print(datas,value)

'''
    Lines 20 to 24 in the provided code snippet explain the usage of the setdefault() function in Python dictionaries. Here's a breakdown of each line:

Line 20: datas = {'1': 123, '2': 566, '3': 899}

This line initializes a dictionary named datas with three key-value pairs. The keys are strings ('1', '2', '3') and their corresponding values are integers (123, 566, and 899).
Line 21: # setdefault() function is used to set a default value for a key if it is not available

This comment explains the purpose of the setdefault() function. It states that setdefault() can be used to provide a default value for a key if that key does not already exist in the dictionary.
Line 22: # it returns the value for the given key if it exists in the dictionary. If not, it

This comment continues explaining the behavior of setdefault(). It indicates that if the specified key exists in the dictionary, the function returns the value associated with that key. If the key does not exist, the function will insert the key with the specified default value and return that default value.
Line 23: value = data.setdefault('11',789)

This line calls the setdefault() method on a dictionary named data (which is actually defined earlier in the code but not shown here). It attempts to access the key '11'. Since '11' does not exist in the data dictionary, it sets '11' to the value 789 and assigns this value to the variable value.
Line 24: print(datas,value)

This line prints the contents of the datas dictionary and the value assigned to the variable value. It shows the original datas dictionary and the result of the setdefault() call.
Overall, these lines demonstrate how setdefault() can be used to ensure a key has a default value if it is not already present in the dictionary.
'''