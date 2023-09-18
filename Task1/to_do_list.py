import tkinter as tk
import tkinter.messagebox
import pickle

tasks = []
task_number = 1

def add_activity():
    global task_number
    activity = entry.get()
    if activity:
        tasks.append(activity)
        listbox.insert(tk.END, f"{task_number}. {activity}")
        entry.delete(0, tk.END)
        task_number += 1
    else:
        tkinter.messagebox.showwarning(title="Attention!!",message="To add activity,please enter some activity!!")
        
def edit_activity():
    selected_index = listbox.curselection()
    if selected_index:
        selected_activity = listbox.get(selected_index)
        new_activity = entry.get()
        if new_activity:
            tasks[selected_index[0]] = new_activity
            listbox.delete(selected_index)
            listbox.insert(selected_index, f"{selected_activity.split('.')[0]}. {new_activity}")
            entry.delete(0, tk.END)
    else:
         tkinter.messagebox.showwarning("Warning", "Please enter a new task.")

def delete_activity():
    selected_index = listbox.curselection()
    if selected_index:
        confirmation = tkinter.messagebox.askyesno("Confirm", "Are you sure you want to delete the selected task?")
        if confirmation:
            listbox.delete(selected_index)
            tasks.pop(selected_index[0])
    else:
        tkinter.messagebox.showwarning("Warning", "Select something to delete")
window = tk.Tk()
window.title("My To-Do List")


listbox = tk.Listbox(window, width=50, bg="white", fg="black")
listbox.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12), width=35)
entry.pack(pady=10)


button_frame = tk.Frame(window)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add", bg="green", fg="white", command=add_activity)
add_button.grid(row=0, column=0, padx=5)

edit_button = tk.Button(button_frame, text="Edit", bg="orange", fg="white", command=edit_activity)
edit_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete", bg="red", fg="white", command=delete_activity)
delete_button.grid(row=0, column=2, padx=5)

window.mainloop()

