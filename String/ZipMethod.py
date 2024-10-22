
key = ["Arpan", "Jalaj", "Sajal", "Shivansh"]
value = [22,22,2,58]
city = ["Betul", "Narmadapuram", "Bhopal", "NArmada par"]

result = zip(key,value,city) 
# if we want to store in dicinory so we use     - dict(zip(key,value))
# Dicinory never take more than 2 variable like this - dict(zip(key,value,city))

result1 = dict(zip(key,value))

# if we want to store in Tuple so we use - tuple(zip(key,value))

result2 = tuple(zip(key,value,city))

print(result)
print(result1)
print(result2)
