# writing data to a file
user=input("Enter text to write to the file: ")
with open('output.txt',"w") as file1:
    file1.write(user+'\n')
print("Data successfully written to output.txt")
# appending data to the file
user2=input("Enter additional text to append: ")
with open('output.txt',"a") as file1:
    file1.write(user2+'\n')
print("Data successfully appended")
# printing the data present in the file
print("\nFinal content of output.txt:")
with open('output.txt',"r") as file1:
    data=file1.read()
    print(data)