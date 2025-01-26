CHATGPT CONVERSATION

**************

make a PYTHON code that compares 2 text documents (e.g. same / different words)
ChatGPT said:
ChatGPT
Here’s a Python script that compares two text documents and highlights the similarities and differences in terms of words. It counts the total number of unique words, common words, and words that are unique to each document. 😊🐍📄✨

python
Copy
Edit
from collections import Counter

def read_file(file_path):
    """Reads the content of a file and returns a list of words."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            words = content.split()
            return [word.strip('.,!?()"\'') for word in words]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found!")
        return []

def compare_documents(file1, file2):
    """Compares two documents and displays common and unique words."""
    # Read and process files
    words1 = read_file(file1)
    words2 = read_file(file2)
    
    if not words1 or not words2:
        return

    # Use Counter for word frequency
    counter1 = Counter(words1)
    counter2 = Counter(words2)

    # Sets for comparison
    set1 = set(counter1.keys())
    set2 = set(counter2.keys())

    # Find common and unique words
    common_words = set1 & set2
    unique_to_file1 = set1 - set2
    unique_to_file2 = set2 - set1

    # Print results
    print(f"Total unique words in {file1}: {len(set1)}")
    print(f"Total unique words in {file2}: {len(set2)}")
    print(f"Common words: {len(common_words)}")
    print(f"Words unique to {file1}: {len(unique_to_file1)}")
    print(f"Words unique to {file2}: {len(unique_to_file2)}")

    # Show some sample results
    print("\nSample of common words:", list(common_words)[:10])
    print(f"Sample of words unique to {file1}:", list(unique_to_file1)[:10])
    print(f"Sample of words unique to {file2}:", list(unique_to_file2)[:10])

# Example usage:
# compare_documents('document1.txt', 'document2.txt')
How to Use
Save this code in a .py file.
Replace 'document1.txt' and 'document2.txt' with the paths to your text documents.
Run the script, and it will print a summary of the comparison, including common words and words unique to each file. 😊💻📜
You can also extend the code to save the output to a file or generate detailed reports if needed. Do you want any further customizations? 😄✨







You said:
now give it a GUI for settings
ChatGPT said:
ChatGPT
Here’s a Python version of the same script with a GUI added using tkinter. It allows you to choose two files for comparison and displays the results in the GUI! 🎨🖥️✨

python
Copy
Edit
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter

def read_file(file_path):
    """Reads the content of a file and returns a list of words."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            words = content.split()
            return [word.strip('.,!?()"\'') for word in words]
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {file_path} not found!")
        return []

def compare_documents(file1, file2):
    """Compares two documents and displays common and unique words."""
    # Read and process files
    words1 = read_file(file1)
    words2 = read_file(file2)
    
    if not words1 or not words2:
        return

    # Use Counter for word frequency
    counter1 = Counter(words1)
    counter2 = Counter(words2)

    # Sets for comparison
    set1 = set(counter1.keys())
    set2 = set(counter2.keys())

    # Find common and unique words
    common_words = set1 & set2
    unique_to_file1 = set1 - set2
    unique_to_file2 = set2 - set1

    # Display results
    results_text.set(
        f"Total unique words in File 1: {len(set1)}\n"
        f"Total unique words in File 2: {len(set2)}\n"
        f"Common words: {len(common_words)}\n"
        f"Words unique to File 1: {len(unique_to_file1)}\n"
        f"Words unique to File 2: {len(unique_to_file2)}\n\n"
        f"Sample of common words: {list(common_words)[:10]}\n"
        f"Sample of words unique to File 1: {list(unique_to_file1)[:10]}\n"
        f"Sample of words unique to File 2: {list(unique_to_file2)[:10]}"
    )

def select_file1():
    global file1_path
    file1_path = filedialog.askopenfilename(title="Select the first file")
    file1_label.config(text=f"File 1: {file1_path}")

def select_file2():
    global file2_path
    file2_path = filedialog.askopenfilename(title="Select the second file")
    file2_label.config(text=f"File 2: {file2_path}")

def compare_files():
    if not file1_path or not file2_path:
        messagebox.showwarning("Warning", "Please select both files before comparing.")
        return
    compare_documents(file1_path, file2_path)

# GUI Setup
root = tk.Tk()
root.title("Text File Comparator")
root.geometry("600x400")

file1_path = None
file2_path = None

# Labels and buttons
file1_label = tk.Label(root, text="File 1: Not selected")
file1_label.pack(pady=5)

file1_button = tk.Button(root, text="Select File 1", command=select_file1)
file1_button.pack(pady=5)

file2_label = tk.Label(root, text="File 2: Not selected")
file2_label.pack(pady=5)

file2_button = tk.Button(root, text="Select File 2", command=select_file2)
file2_button.pack(pady=5)

compare_button = tk.Button(root, text="Compare Files", command=compare_files)
compare_button.pack(pady=10)

results_text = tk.StringVar()
results_label = tk.Label(root, textvariable=results_text, justify="left", wraplength=550)
results_label.pack(pady=10)

# Run the GUI
root.mainloop()
How to Use
Save this script to a .py file and run it.
Use the "Select File 1" and "Select File 2" buttons to choose two text files.
Click "Compare Files" to see the results displayed in the window.
Features
Simple GUI for file selection. 🖱️📂
Displays comparison results directly in the app. 📝
Highlights unique and common words. ✨
Want me to enhance it with any other feature, like saving the results to a file or more advanced visualizations? 😊
