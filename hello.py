import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("System Admin Project")
root.geometry("500x300")
root.configure(bg="#f0f0f0")

# Title label
title_label = ttk.Label(root, text="System Admin Project", font=("Helvetica", 18, "bold"))
title_label.pack(pady=20)

# Message label
message = "How are you students.\nThis is System Admin project."
message_label = ttk.Label(root, text=message, font=("Helvetica", 14), justify="center")
message_label.pack(pady=20)

# Exit button
exit_button = ttk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
