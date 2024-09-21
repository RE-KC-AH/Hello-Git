import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def modify_row():
    item = tree.selection()
    if not item:
        messagebox.showwarning("提示", "没有选择任何一行")
        return
    target_id = item[0]
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    _id = id_entry.get()
    hobby = hobby_entry.get()
    gpa = gpa_entry.get()
    tree.item(target_id, values = (name, age, gender, _id, hobby, gpa))

def add_row():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    _id = id_entry.get()
    hobby = hobby_entry.get()
    gpa = gpa_entry.get()
    tree.insert("", tk.END, values = (name, age, gender, _id, hobby, gpa))

def del_row():
    item = tree.selection()
    if not selection:
        messagebox.showwarning("提示","没有选择任何一行")
        return
    tree.delete(item[0])

window = tk.Tk()
window.title("学生管理")

columns = ("名字","年龄","性别","学号","爱好","绩点")
tree = ttk.Treeview(window, columns = columns, show = "headings")

for item in columns:
    tree.heading(item, text = item)
    tree.column(item, width = 100)

tree.pack()

tk.Label(window, text = "名字").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text = "年龄").pack()
age_entry = tk.Entry(window)
age_entry.pack()

tk.Label(window, text = "性别").pack()
gender_entry = ttk.Combobox(window, value = ["男","女","沃尔玛购物袋"], state = "readonly")
gender_entry.pack()

tk.Label(window, text = "学号").pack()
id_entry = tk.Entry(window)
id_entry.pack()

tk.Label(window, text = "爱好").pack()
hobby_entry = tk.Entry(window)
hobby_entry.pack()

tk.Label(window, text = "绩点").pack()
gpa_entry = tk.Entry(window)
gpa_entry.pack()

modify_button = tk.Button(window, text = "修改", command = modify_row)
modify_button.pack()

add_button = tk.Button(window, text = "增加", command = add_row)
add_button.pack()

del_button = tk.Button(window, text = "增加", command = del_row)
del_button.pack()

window.mainloop()
