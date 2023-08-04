def file_recording(text: str):
    f = open("myfile.txt", "x")
    f.write(text)
    f.close()


#file_recording(text = input("Enter you text: "))