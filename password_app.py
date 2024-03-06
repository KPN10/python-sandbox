#!/usr/bin/python3

import tkinter as tk
from library.password import PasswordWindow

class Application:
    def __init__(self):
        print("hi")
        self.password = ""
        self.window = tk.Tk()
        self.buttonTest =\
            tk.Button(self.window, text="test", command=self.somePrivelegedAction).pack()
        self.buttonQuit =\
            tk.Button(self.window, text="quit", command=self.quit).pack()
        self.window.mainloop()

    def __del__(self):
        print("bye bye")

    def quit(self):
        self.window.destroy()

    def somePrivelegedAction(self):
        passwin = PasswordWindow()
        self.password = passwin.getPassword()
        del passwin
        print("Password:", self.password)
        
def main():
    app = Application()

if __name__ == "__main__":
    main()
