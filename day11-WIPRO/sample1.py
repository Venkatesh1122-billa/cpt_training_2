try:
    file = open('File1.txt')
    str = file.readline()
    print(str)
    print(strr)
except IOError:
    print("Error occured during input take ....")
else:
    print("Successfully fetched the data ......")    