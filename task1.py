try:
    with open ("sample.txt", "rt") as fh:
        i=1
        for line in fh:
            print(f"Line{i}: {(line).rstrip()}")
            i+=1
    
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
