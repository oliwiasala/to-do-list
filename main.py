from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("To Do List")
window.geometry("280x440")
window.resizable(width=False, height=False)
window.config(bg="#223441")
window.eval("tk::PlaceWindow . center")

font = "Courier"


def show_task_list():
    with open("task_list.txt", "r") as task_list_content:
        content = task_list_content.read()
        task_listbox.insert(END, content)


def add_task():
    task = task_input.get()

    with open("task_list.txt", "a") as task_list:
        task_list.write(f"{task}\n")

    if len(task) == 0:
        messagebox.showwarning("Empty Entry", "Enter a task")
    else:
        task_input.delete(0, END)
        task_listbox.insert(END, task)


def delete():
    task_listbox.delete(ANCHOR)
    if (s.curselection() for s in task_listbox):
        messagebox.showwarning("Cannot delete", "No task selected")


def delete_all():
    task_listbox.delete(0, END)
    with open("task_list.txt", "w"):
        pass


task_label = Label(text="Enter a task:", font=(font, 18), bg="#223441", fg="white")
task_label.place(x=50, y=30)

task_input = Entry(width=22, font=font, borderwidth=0)
task_input.place(x=50, y=60)

task_listbox = Listbox(height=13, font=font, width=23, bd=0, selectmode="SINGLE")
task_listbox.place(x=50, y=93)

add_task_button = Button(text="Add task", font=font, width=22, command=add_task)
add_task_button.place(x=52, y=290)

delete_button = Button(text="Delete", font=font, width=22, command=delete)
delete_button.place(x=52, y=320)

delete_all_button = Button(text="Delete all", font=font, width=22, command=delete_all)
delete_all_button.place(x=52, y=350)

exit_button = Button(text="Exit", font=font, width=22, command=window.quit)
exit_button.place(x=52, y=380)

show_task_list()

window.mainloop()

# Make messageboxes and saving in csv
