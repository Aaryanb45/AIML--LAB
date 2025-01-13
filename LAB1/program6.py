fruits=["APPLE","BANANAN","MANGO","ORANGE"]
print("Accessing elemnts using indexing")
print(f"first Fruits: {fruits[0]}")
print(f"second Fruits: {fruits[2]}")
print(f"third Fruits: {fruits[-1]}")

fruits[1]="Kiwies"
print(f"modified list: {fruits}")

fruits.remove("MANGO")
print(f"modified list: {fruits}")

length=len(fruits)
print(length)

fruits.sort()
print(f"sorted fruits list sre/is: {fruits}")