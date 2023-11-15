import tkinter as tk
from tkinter import filedialog

class ToDoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("600x600")
        self.title("To Do List")

        self.create_widgets()

    def create_widgets(self):
        self.task_input = tk.Entry(self, width = 30, font = ("Comic Sans MS", 24))
        self.task_input.pack(pady = 10)

        self.add_task_button = tk.Button(self, text = "Add Task", command = self.add_task, font = ("Comic Sans MS", 15))
        self.add_task_button.pack(pady = 5)

        self.tasks_listBox = tk.Listbox(self, selectmode = tk.SINGLE, font = ("Comic Sans MS", 15))
        self.tasks_listBox.pack(pady = 5)
        
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady = 5)
        
        self.edit_task_button = tk.Button(self.button_frame, text = "Edit Task", command = self.edit_task, font = ("Comic Sans MS", 15))
        self.edit_task_button.grid(row = 0, column = 0, pady = 5)

        self.delete_task_button = tk.Button(self.button_frame, text = "Delete Task", command = self.delete_task, font = ("Comic Sans MS", 15))
        self.delete_task_button.grid(row = 0, column = 1, pady = 5)

        self.save_button = tk.Button(self, text = "Save", command = self.save_tasks, font = ("Comic Sans MS", 15))
        self.save_button.pack(pady = 5)

        self.load_button = tk.Button(self, text = "Load", command = self.load_tasks, font = ("Comic Sans MS", 15))
        self.load_button.pack(pady = 5)

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks_listBox.insert(tk.END, task)
            self.task_input.delete(0, tk.END)

    def edit_task(self):
        task_index = self.tasks_listBox.curselection()
        if task_index:
            new_task = self.task_input.get()
            if new_task:
                self.tasks_listBox.delete(task_index)
                self.tasks_listBox.insert(task_index, new_task)
                self.task_input.delete(0, tk.END)

    def delete_task(self):
        task_index = self.tasks_listBox.curselection()
        if task_index:
            self.tasks_listBox.delete(task_index)

    def save_tasks(self):
        tasks = self.tasks_listBox.get(0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension = ".txt")
        if file_path:
            with open(file_path, 'w') as file:
                for task in tasks:
                    file.write(task + '\n')

    def load_tasks(self):
        file_path = filedialog.asksaveasfilename(filetypes = [("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                tasks = [line.strip() for line in file.readlines()]

            self.tasks_listBox.delete(0, tk.END)
            
            for task in tasks:
                self.tasks_listBox.insert(tk.END, task)

if __name__ == "__main__":
    app = ToDoListApp()
    app.mainloop()