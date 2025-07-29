import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd


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

def  predict_interaction():
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


# User interface Design
app = tk.Tk()
app.title("Drug-Target Prediction System")
app.geometry("700x600")
app.config(bg="teal")

# UI Layout
tk.Button(app, text="Load Dataset",command=load_dataset, bg="#2196F3", fg="white", width=20)\
    .place(relx=0.35, rely=0.05)

tk.Label(app, text="Drug Name:", bg="#f0f0f0").place(relx=0.05, rely=0.15)
drug_entry = tk.Entry(app, width=50)
drug_entry.place(relx=0.3, rely=0.15)

tk.Label(app, text="Target Name:", bg="#f0f0f0").place(relx=0.05, rely=0.22)
target_entry = tk.Entry(app, width=50)
target_entry.place(relx=0.3, rely=0.22)

tk.Button(app, text=" Predict Interaction", command=predict_interaction, bg="#4CAF50", fg="white", width=20)\
    .place(relx=0.05, rely=0.3)

tk.Button(app, text=" Visual Interaction", bg="#FF9800", fg="white", width=20)\
    .place(relx=0.4, rely=0.3)

tk.Button(app, text=" Clear Output", bg="#E91E63", fg="white", width=15)\
    .place(relx=0.05, rely=0.37)

tk.Button(app, text=" Save Output", bg="#9C27B0", fg="white", width=15)\
    .place(relx=0.4, rely=0.37)

# Output Box
result_box = tk.Text(app, height=20, width=85)
result_box.place(relx=0.05, rely=0.45)

app.mainloop()
