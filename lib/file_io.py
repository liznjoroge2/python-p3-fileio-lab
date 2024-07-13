def write_file(file_name, file_content):
    # Ensure the file has a .txt extension
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    
    # Write the content to the file
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, file_content):
    # Ensure the file has a .txt extension
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    
    # Append the content to the file
    with open(file_name, 'a') as file:
        file.write(file_content)

def read_file(file_name):
    # Ensure the file has a .txt extension
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    
    # Read the content from the file
    with open(file_name, 'r') as file:
        return file.read()
