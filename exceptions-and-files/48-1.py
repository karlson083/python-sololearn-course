file = open("4801.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("4801.txt", "r")
print(file.read())
file.close()