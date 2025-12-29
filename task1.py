try:
    with open ("sample.txt", "rt") as fh:
        i=1
        for line in fh:
            print(f"Line{i}: {(line).rstrip()}")
            i+=1
    
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")



#Sample Output (File exists)
'''
Line1: This is a sample text file.
Line2: It contains multiple lines.
Line3: Bye
Line4: Have a good day
'''

#Sample Output (File doesn not exist)
'''
Error: The file 'sample.txt' was not found.
'''
