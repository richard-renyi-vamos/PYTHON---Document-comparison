import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

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
    words1 = read_file(file1)
    words2 = read_file(file2)

    if not words1 or not words2:
        return

    counter1 = Counter(words1)
    counter2 = Counter(words2)

    set1 = set(counter1.keys())
    set2 = set(counter2.keys())

    common_words = set1 & set2
    unique_to_file1 = set1 - set2
    unique_to_file2 = set2 - set1

    common_freq = {word: counter1[word] + counter2[word] for word in common_words}
    top_common = sorted(common_freq.items(), key=lambda x: x[1], reverse=True)[:10]

    results = (
        f"📄 Total words in File 1: {len(words1)}\n"
        f"📄 Total words in File 2: {len(words2)}\n"
        f"🔠 Unique words in File 1: {len(set1)}\n"
        f"🔠 Unique words in File 2: {len(set2)}\n"
        f"🤝 Common words: {len(common_words)}\n"
        f"📌 Unique to File 1: {len(unique_to_file1)}\n"
        f"📌 Unique to File 2: {len(unique_to_file2)}\n\n"
        f"🔝 Top Common Words (with frequencies):\n"
        + "\n".join([f"   {w}: {f}" for w, f in top_common]) + "\n\n"
        f"🎯 Sample Common Words: {list(common_words)[:10]}\n"
        f"📍 Sample Unique to File 1: {list(unique_to_file1)[:10]}\n"
        f"📍 Sample Unique to File 2: {list(unique_to_file2)[:10]}"
    )
    results_text.set(results)
    current_comparison_result.set(results)  # for saving

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

def save_results():
    if not current_comparison_result.get():
        messagebox.showinfo("Info", "No comparison results to save.")
        return
    path = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text files", "*.txt")])
    if path:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(current_comparison_result.get())
        messagebox.showinfo("Saved", f"Results saved to {path}")

def reset_fields():
    global file1_path, file2_path
    file1_path = None
    file2_path = None
    file1_label.config(text="File 1: Not selected")
    file2_label.config(text="File 2: Not selected")
    results_text.set("")
    current_comparison_result.set("")

def generate_wordcloud():
    if not file1_path or not file2_path:
        messagebox.showinfo("Info", "Compare two files first.")
        return
    words1 = read_file(file1_path)
    words2 = read_file(file2_path)
    text = " ".join(words1 + words2)
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Combined Word Cloud", fontsize=16)
    plt.tight_layout()
    plt.show()

# GUI Setup
root = tk.Tk()
root.title("Text File Comparator Pro ✨")
root.geometry("650x600")

file1_path = None
file2_path = None

file1_label = tk.Label(root, text="File 1: Not selected")
file1_label.pack(pady=5)

file1_button = tk.Button(root, text="Select File 1 📂", command=select_file1)
file1_button.pack(pady=5)

file2_label = tk.Label(root, text="File 2: Not selected")
file2_label.pack(pady=5)

file2_button = tk.Button(root, text="Select File 2 📂", command=select_file2)
file2_button.pack(pady=5)

compare_button = tk.Button(root, text="Compare Files 🔍", command=compare_files)
compare_button.pack(pady=10)

results_text = tk.StringVar()
current_comparison_result = tk.StringVar()
results_label = tk.Label(root, textvariable=results_text, justify="left", wraplength=600)
results_label.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=5)

save_button = tk.Button(buttons_frame, text="Save Results 💾", command=save_results)
save_button.grid(row=0, column=0, padx=10)

cloud_button = tk.Button(buttons_frame, text="Show Word Cloud ☁️", command=generate_wordcloud)
cloud_button.grid(row=0, column=1, padx=10)

reset_button = tk.Button(buttons_frame, text="Reset 🧹", command=reset_fields)
reset_button.grid(row=0, column=2, padx=10)

root.mainloop()
