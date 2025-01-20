#Q3
# oCreate a list and a tuple.
# oTry to modify an element in both the list and the tuple.
# oObserve the results and explain the difference.
mylist=[45,18,7,99]
mytuple=(45,18,7,99)
mylist[2] = 10
print("Modified list:", mylist)  
try:
    mytuple[2] = 10
except TypeError as e:
    print("Error:", e)
print("Original tuple:", mytuple)