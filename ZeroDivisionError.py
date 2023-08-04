try:
    a = int(input("Enter number: "))
    x = 25
    print(25 / a)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
print("success")