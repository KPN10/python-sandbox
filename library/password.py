import tkinter as tk

class PasswordWindow:
    def __init__(self):
        self.password = ""
        self.window = tk.Tk()
        self.window.geometry("300x100")
        self.window.title("Input root password")
        self.label = tk.Label(self.window, text="Enter Password").pack()
        self.entry = tk.Entry(self.window, show="*")
        self.entry.pack()
        self.button = tk.Button(self.window, text="ok", command=self.readPassword).pack()
        self.window.mainloop()

    def __del__(self):
        pass
        
    def readPassword(self):
        self.password = self.entry.get()
        self.window.destroy()
        self.window.quit()

    def getPassword(self):
        return self.password
