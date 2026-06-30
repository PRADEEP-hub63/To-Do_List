import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Refresh listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["done"] else "✘"
        listbox.insert(tk.END, f"[{status}] {task['title']}")

# Add task
def add_task(event=None):
    title = entry.get()
    if title.strip() == "":
        messagebox.showwarning("Warning", "Please type a task in the text box above, then click Add Task or press Enter.")
        entry.focus_set()
        return
    tasks.append({"title": title.strip(), "done": False})
    entry.delete(0, tk.END)
    save_tasks()
    update_listbox()
    entry.focus_set()

# Delete task
def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        save_tasks()
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

# Mark as done
def mark_done():
    try:
        index = listbox.curselection()[0]
        tasks[index]["done"] = True
        save_tasks()
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task!")

# Clear all tasks
def clear_tasks():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        tasks.clear()
        save_tasks()
        update_listbox()

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.resizable(False, False)

tasks = load_tasks()

# Title
header_label = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"))
header_label.pack(pady=10)

# Entry
entry_label = tk.Label(root, text="Type your task here:", font=("Arial", 11))
entry_label.pack(pady=(0, 5))

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=5)
entry.bind("<Return>", add_task)
entry.focus_set()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

done_btn = tk.Button(btn_frame, text="Mark Done", width=12, command=mark_done)
done_btn.grid(row=0, column=1, padx=5)

del_btn = tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task)
del_btn.grid(row=1, column=0, padx=5, pady=5)

clear_btn = tk.Button(btn_frame, text="Clear All", width=12, command=clear_tasks)
clear_btn.grid(row=1, column=1, padx=5, pady=5)

# Listbox
listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
listbox.pack(pady=10)

# Load existing tasks
update_listbox()

# Run app
root.mainloop()
