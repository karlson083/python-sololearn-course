try:
    with open("test.txt") as f:
        print(f.read())
except:
    print("Error")