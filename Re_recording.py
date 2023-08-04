#file_recording(text: str):\
f1 = open("myfile.txt", "r")
f2 = open("myfile2.txt", "x")
x1 = f1.read()
f2.write(x1)
f1.close()
f2.close()


#file_recording(text = input("Enter you text: "))