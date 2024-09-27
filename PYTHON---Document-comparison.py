import difflib

def read_file(file_path):
    """Reads the contents of a file and returns them as a list of lines."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def compare_files(file1_path, file2_path):
    """Compares two text files and returns the differences."""
    file1_lines = read_file(file1_path)
    file2_lines = read_file(file2_path)
    
    diff = difflib.unified_diff(file1_lines, file2_lines, lineterm='', 
                                fromfile='File 1', tofile='File 2')
    
    return list(diff)

def save_diff(diff, output_path):
    """Saves the differences to a new file."""
    with open(output_path, 'w', encoding='utf-8') as diff_file:
        diff_file.writelines(diff)

# Example usage:
file1_path = 'file1.txt'  # Replace with the actual path of the first file
file2_path = 'file2.txt'  # Replace with the actual path of the second file
output_diff_path = 'diff_output.txt'  # Path to save the differences

differences = compare_files(file1_path, file2_path)

# Print differences to the console
for line in differences:
    print(line)

# Save differences to a file
save_diff(differences, output_diff_path)
