# Input number
number = int(input("Enter a number: "))

if number <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, number):
        if number % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("It is a Prime Number")
