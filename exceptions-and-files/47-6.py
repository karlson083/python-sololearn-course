import os
clear = lambda: os.system('cls')
clear()
file = open("filename.txt","r")
str = file.read()
print(len(str))
file.close()