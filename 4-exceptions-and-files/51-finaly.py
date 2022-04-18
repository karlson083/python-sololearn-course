import os
clear = lambda: os.system('cls')
clear()

file = open("filename.txt","r")
count_str = len(file.readlines())
file.close()

file = open("filename.txt","r")
#print(count_str)
for i in range(count_str):
    first_ch = file.read(1)
    count = str(len(file.readline()) )
    print(first_ch+count)
file.close()