import os
clear = lambda: os.system('cls')
clear()

file = open("filename.txt","r")
print(file.readlines())


file.close()