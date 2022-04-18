import os
clear = lambda: os.system('cls')
clear()
file = open("filename.txt","r")

file.read()
print("Re-Read")
print(file.read())
print("Finished")

file.close()