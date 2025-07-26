import tkinter as tk

# User interface Design
app = tk.Tk()
app.title("Drug-Target Prediction System")
app.geometry("700x600")
app.config(bg="teal")

# UI Layout
tk.Button(app, text="Load Dataset", bg="#2196F3", fg="white", width=20)\
    .place(relx=0.35, rely=0.05)

tk.Label(app, text="Drug Name:", bg="#f0f0f0").place(relx=0.05, rely=0.15)
drug_entry = tk.Entry(app, width=50)
drug_entry.place(relx=0.3, rely=0.15)

tk.Label(app, text="Target Name:", bg="#f0f0f0").place(relx=0.05, rely=0.22)
target_entry = tk.Entry(app, width=50)
target_entry.place(relx=0.3, rely=0.22)

tk.Button(app, text=" Predict Interaction",  bg="#4CAF50", fg="white", width=20)\
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