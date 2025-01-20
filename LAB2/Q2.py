# Q2.  Create and manipulate dictionaries.
# Create a dictionary to store information about a person (name, age, city).
# Access values using keys.
# Add a new key-value pair to the dictionary.
# Modify an existing value.
# Check if a key exists in the dictionary.
# Get a list of all keys and values.

person={"name":"Aryan","age":21,"Email":"aryanbansal182004@gmail.com","city":"Mount Abu"}
print("Name",person["name"])
print("Age",person["age"])
print("Email",person["Email"])
print("City Belongs to",person["city"])
person["gender"] = "male"
print("Updated dictionary with gender:", person)
person["age"] = 23
print("Updated dictionary with modified age:", person)
if "city" in person:
    print("Key 'city' exists in the dictionary")
keys = person.keys()
values = person.values()
print("Keys:", list(keys))
print("Values:", list(values))