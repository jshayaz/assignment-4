# Reading data from a file
try:
    with open("sample.txt", "r") as file1:
        data=file1.read()
        print(data)
# file not found error handling
except FileNotFoundError:
    print("Error: The file 'sample.txt' not found.")