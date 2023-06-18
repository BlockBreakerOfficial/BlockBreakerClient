import tkinter as tk
from PIL import ImageTk, Image

import src.utils
from src.windows.register import Register

data = src.utils.load()

root = tk.Tk()
root.title("BlockBreaker Client")
root.geometry("800x600")
root.iconbitmap("assets/icon.ico")

widget = tk.Label(root, text="Enter your BlockBreaker license key in the popup window.", font=("Ubuntu", 16))
widget.place(x=10, y=10)

icon = Image.open("assets\\icon.png")
icon = icon.resize((256, 256), Image.Resampling.NEAREST)
icon = ImageTk.PhotoImage(icon)
widget = tk.Label(image=icon)
widget.image = icon
widget.place(x=100, y=244)

widget = tk.Label(root, text="BlockBreakerClient", font=("Ubuntu", 16))
widget.place(x=386, y=348)
widget = tk.Label(root, text="© TechnoDot 2023", font=("Ubuntu", 16))
widget.place(x=386, y=380)

if True:
    register_window = Register()

root.mainloop()