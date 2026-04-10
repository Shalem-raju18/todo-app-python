import tkinter as tk
from tkinter import messagebox

FILE_NAME = "tasks.txt"

# Load tasks
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

# Save tasks
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add task
def add_task(event=None):
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Enter a task!")

# Delete task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task!")

# Mark as completed
def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(tk.END, "✔ " + task)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task!")

# Main window
root = tk.Tk()
root.title("Advanced To-Do App")
root.geometry("450x500")
root.config(bg="#2c3e50")

# Title
title = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="#2c3e50", fg="white")
title.pack(pady=10)

# Entry box
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)
entry.bind("<Return>", add_task)

# Buttons frame
frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=10)

add_btn = tk.Button(frame, text="Add", width=10, command=add_task, bg="#27ae60", fg="white")
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(frame, text="Delete", width=10, command=delete_task, bg="#c0392b", fg="white")
delete_btn.grid(row=0, column=1, padx=5)

done_btn = tk.Button(frame, text="Done", width=10, command=mark_done, bg="#2980b9", fg="white")
done_btn.grid(row=0, column=2, padx=5)

# Listbox with scrollbar
frame_list = tk.Frame(root)
frame_list.pack()

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame_list, width=40, height=15, font=("Arial", 12), yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

# Load tasks
load_tasks()

# Run app
root.mainloop()