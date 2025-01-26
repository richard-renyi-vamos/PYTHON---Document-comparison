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
