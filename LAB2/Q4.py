# oTake a number as input from the user.
# oUse a for loop to iterate from 1 to 10.
# oCalculate the product of the input number and the current iteration.
# oPrint the multiplication table.
number = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")