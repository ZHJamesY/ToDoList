import tkinter as tk
import os

root = tk.Tk()

window_w = 500
window_h = 600

center_w = root.winfo_screenwidth()/2 - window_w/2
center_h = root.winfo_screenheight()/2 - window_h/2

root.title("To-Do-List")

# width x height + appear position x + appear position y
root.geometry("%dx%d+%d+%d" % (window_w, window_h, center_w, center_h)) 

#disable window resize function: False, False
root.resizable(0, 0)

# Task data
task_list = []

# Add text to listbox
def addTask():
    task = task_entry.get()
    task_entry.delete(0, tk.END)
    if task:
        with open("list/tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(tk.END, task)

# Delete listbox's text
def deleteTask():
    global task_list
    task = str(listbox.get(tk.ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("list/tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(tk.ANCHOR)

# access txt file, append text to task_list and insert to listbox
# if no list folder or txt file, create a new folder and/or txt file
def openTaskFile():
    try:
        global task_list
        with open("list/tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(tk.END, task)
    except:
        path = "list"
        os.mkdir(path)
        file = open("list/tasklist.txt", "w")
        file.close
        
#top frame
frame = tk.Canvas(root, height = 50, width = 500, bg = "#32405b")
frame.pack()

#background 
# background = tk.Canvas(root, height = 600, width = 500, bg = "#234A61")
# background.pack()

#icon
window_icon = tk.PhotoImage(file = "image/icon.png")
root.iconphoto(False, window_icon)

#heading in top frame
heading = tk.Label(root, text="All Task", font = "arial 20 bold", fg= "white", bg = "#32405b")
heading.place(x = 200, y = 10)

#input field: canvas
input_bar = tk.Canvas(root, width = 500, height = 52, bg = "white")
input_bar.place(x = 0, y = 100)

#input field: text box
task = tk.StringVar()
task_entry = tk.Entry(input_bar, width = 24, font = "arial 20", bd = 0, insertbackground = "black", fg = "black", bg = "white")
task_entry.place(x = 10, y = 7)
task_entry.focus()

#input field: the add button
button = tk.Button(input_bar, text = "ADD", font = "arial 20 bold", width = 6, bg = "#5a95ff", fg = "#fff", bd = 0, command = addTask)
button.place(x = 400, y = 2)

#list box: background frame
list = tk.Frame(root, bd = 3, width = 500, height = 200, bg = "#32405b")
list.pack(pady = (113, 0))

#list box: text box
listbox = tk.Listbox(list, font = ("arial", 12), width = 52, height = 18, bg = "#32405b", fg = "white", cursor = "hand2")
listbox.pack(side = tk.LEFT, padx = 2)

#list box: scrollbar
scrollbar = tk.Scrollbar(list)
scrollbar.pack(side = tk.RIGHT, fill = tk.BOTH)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

openTaskFile()


#delete: clickable icon
delete_icon = tk.PhotoImage(file = "image/bin.png")
tk.Button(root, image = delete_icon, bd = 0, command = deleteTask).pack(side = tk.BOTTOM, pady = 15)


root.mainloop()




