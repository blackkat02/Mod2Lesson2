try:
    a = int(input("Enter number1: "))
    b = int(input("Enter number1: "))
    print(a + b)
except ValueError:
    print("Invalid number. Enter the correct number")
print("success")