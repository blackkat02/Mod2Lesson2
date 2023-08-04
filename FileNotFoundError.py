try:
    text = open("ValueError.py")
except FileNotFoundError:
    print("Error")
print("success")