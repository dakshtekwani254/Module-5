#Task 2: Write and Append Data to a File


with open ("output.txt", "wt") as fh:
    data=input("Enter text to write to the file: ")
    fh.write(data + '\n')
    print("Data successfully written to 'output.txt'.\n")

with open ("output.txt", "at") as fh:
    data=input("Enter additional text to append: ")
    fh.write(data + '\n')
    print("Data successfully appended.\n")

with open ("output.txt","rt") as fh:
    print("Final content of 'output.txt': ")
    for line in fh:
        print(line.rstrip())
    
#Sample Output
'''
Enter text to write to the file: Hello, Python!
Data successfully written to 'output.txt'.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of 'output.txt': 
Hello, Python!
Learning file handling in Python.
'''
