import os
clear = lambda: os.system('cls')
clear()
with open("filename.txt") as f:
    print(f.read())