#Reading data from the file.
try:
    with open("sample.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: sample.txt file not found.")
