def line_del(x: int):
    fr = open("myfile.txt", "r")
    lines = fr.readlines()
    y = 1
    f2 = open("myfile2.txt", "w")
    for i in lines:
        if y != x:
            f2.write(f"{i}")
        elif y == x:
            pass
        y += 1
    f2.close()
    fr.close()


line_del(x = int(input("Enter your line number : ")))



