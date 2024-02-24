# Specify the file path
file_path = './data.txt'

# Open the file in read mode ('r' for read)
with open(file_path, 'r') as file:
    # Read the entire content of the file into a string
    content = file.read()

    # Alternatively, you can read the file line by line
    # lines = file.readlines()
    
    # Or read just one line at a time
    # line = file.readline()

# Now, 'content' variable contains the content of the file
print(content)