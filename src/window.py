import tkinter as tk

class Window():
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("BlockBreaker Client")
        self.root.geometry("800x600")
        self.root.iconbitmap("assets/icon.ico")
        self.setup()
        self.root.mainloop()
    
    def title(self, title):
        self.root.title(title)
    
    def size(self, size):
        self.root.geometry(size)
    
    def resizeLock(self):
        self.root.resizable(False, False)
    
    def setup(self):
        pass
