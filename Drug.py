import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Global dataset
df = None

# Load dataset function
def load_dataset():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
            messagebox.showinfo("Success", "Dataset loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load dataset:\n{e}")

# Rule-based prediction function
def predict_interaction():
    if df is None:
        messagebox.showwarning("Dataset Not Loaded", "Please load a dataset first.")
        return

    drug_input = drug_entry.get().strip().lower()
    target_input = target_entry.get().strip().lower()

    results = []

    for index, row in df.iterrows():
        drug = str(row.get("drugname", "")).strip().lower()
        target = str(row.get("targetname", "")).strip().lower()
        interaction = str(row.get("interactionlevel", "")).strip()

        if drug_input and drug_input in drug:
            results.append(f"{row['drugname']} targets {row['targetname']} ({interaction})")
        elif target_input and target_input in target:
            results.append(f"{row['drugname']} targets {row['targetname']} ({interaction})")

    result_box.delete("1.0", tk.END)
    if results:
        for res in results:
            result_box.insert(tk.END, res + "\n")
    else:
        result_box.insert(tk.END, "No interaction found.")

# Visualization function
def visualize_network():
    global df
    if df is None:
        messagebox.showerror("Error", "Please load a dataset first.")
        return

    drug_col = next((col for col in df.columns if 'drug' in col), None)
    target_col = next((col for col in df.columns if 'target' in col), None)

    if drug_col is None or target_col is None:
        messagebox.showerror("Error", "Drug or Target column not found.")
        return

    try:
        G = nx.Graph()
        for _, row in df.iterrows():
            G.add_edge(row[drug_col], row[target_col])

        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=10)
        plt.title("Drug-Target Network")
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Visualization failed:\n{str(e)}")

# Clear output
def clear_output():
    result_box.delete("1.0", tk.END)

# Save output
def save_output():
    content = result_box.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("No Output", "Nothing to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Success", f"Output saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")

# GUI setup
app = tk.Tk()
app.title("Drug-Target Prediction System")
app.geometry("700x600")
app.config(bg="teal")

# GUI layout using relx, rely
tk.Button(app, text="Load Dataset", command=load_dataset, bg="#2196F3", fg="white", width=20)\
    .place(relx=0.35, rely=0.05)

tk.Label(app, text="Drug Name:", bg="#f0f0f0").place(relx=0.05, rely=0.15)
drug_entry = tk.Entry(app, width=50)
drug_entry.place(relx=0.3, rely=0.15)

tk.Label(app, text="Target Name:", bg="#f0f0f0").place(relx=0.05, rely=0.22)
target_entry = tk.Entry(app, width=50)
target_entry.place(relx=0.3, rely=0.22)

tk.Button(app, text=" Predict Interaction", command=predict_interaction, bg="#4CAF50", fg="white", width=20)\
    .place(relx=0.05, rely=0.3)

tk.Button(app, text=" Visual Interaction", command=visualize_network, bg="#FF9800", fg="white", width=20)\
    .place(relx=0.4, rely=0.3)

tk.Button(app, text=" Clear Output", command=clear_output, bg="#E91E63", fg="white", width=15)\
    .place(relx=0.05, rely=0.37)

tk.Button(app, text=" Save Output", command=save_output, bg="#9C27B0", fg="white", width=15)\
    .place(relx=0.4, rely=0.37)

# Output Box
result_box = tk.Text(app, height=20, width=85)
result_box.place(relx=0.05, rely=0.45)

app.mainloop()


