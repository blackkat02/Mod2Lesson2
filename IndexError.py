b = int(input("Enter an index from 1to 10: "))
a = range(1, 11)
try:
    print(a[b])
except IndexError:
    print("Invalid index. Enter the correct index")
print(b)