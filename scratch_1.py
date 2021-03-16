# Initialize and declare
dict = {
    "brand": "volksvagen",
    "model" : "vento",
    "year": 1994
}
# print(dict)

# Access items
model = dict["model"]
model = dict.get("model")

# Change value
dict["year"] = 2020
dict["engine"] = 1.9
print(dict)

# Loop through
for x in dict:
    print(x) #keys
for x in dict:
    print(dict[x]) #values
for x in dict.values():
    print(x) #values
for x,y in dict.items():
    print(x,y) # key and value

#check if key exists
if "model2" in dict:
    print("key exists")
else:
    print("key doesn't exist")

#dictionary length
print(len(dict))

#removing elements from dictionary
print(dict)
dict.pop('brand')
print(dict)
dict.clear()
print(dict)

#string formatting
for x,y in dict.items():
    print("{:<30} | {:>20}".format(x,y))