dictionary =  {"Apple":"red","grape":"purple","mango":"yellow"}

print(dictionary)

print(dictionary["Apple"])

print(dictionary.get("Orange"))

for value in dictionary.values():
    print(value)

for key,value in dictionary.items():
    print(key,value)

