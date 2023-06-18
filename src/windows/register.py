import tkinter as tk
import tkinter.ttk as ttk

from ..window import *

class Register(Window):
    def setup(self):
        self.resizeLock()
        self.root.configure(background="#333333")
        frame = tk.Frame(self.root)

        self.code = ["X" for i in range(0, 25)]
        self.inputs = []
        j = 0

        for i in range(0, 25):
            widget = tk.Text(frame, background="#333333", foreground="#00acdb", insertbackground="#00acdb", borderwidth=0, font=("OCR A Extended", 20), height=1, width=1)
            widget.grid(row=0, column=i+j)
            widget.bind("<KeyRelease>", self.keyRelease)
            self.inputs.append(widget)

            if i % 5 == 4 and i != 24:
                label = tk.Label(frame, background="#333333", foreground="#00acdb", font=("OCR A Extended", 20), text="-")
                label.grid(row=0, column=i+j+1)
                j += 1

        frame.place(x=400, y=100, anchor=tk.CENTER)
        self.inputs[0].focus_set()

        self.accepted = tk.IntVar()
        widget = tk.Checkbutton(self.root, text="By checking the box to the left, you consent to the Terms of Service and our Privacy Policy.", background="#333333", foreground="#00acdb", variable=self.accepted, onvalue=1, offvalue=0)
        widget.place(x=400, y=200, anchor=tk.CENTER)

        widget = tk.Button(self.root, text="Confirm", background="#00acdb", foreground="#ffffff", font=("OCR A Extended", 20), command=self.confirm)
        widget.place(x=400, y=300, anchor=tk.CENTER)

        self.progress = ttk.Progressbar(self.root, orient="horizontal", mode="indeterminate", length=300)
        self.progress.place(x=400, y=400, anchor=tk.CENTER)
        self.progress["value"] = 0
    
    def keyRelease(self, event: tk.Event):
        if not event.char.isalnum() and event.keycode != 8:
            event.widget.delete("1.0", "end")
            return
        if event.keycode != 8:
            element = event.widget
            found = False
            x = -1
            for widget in self.inputs:
                if found:
                    widget.focus_set()
                    break
                if widget == element:
                    found = True
                    element.delete("1.0", "end")
                    element.insert("1.0", event.char.upper())
                x += 1
            self.code[x] = event.char.upper()
            print(self.getCode())
        else:
            element = event.widget
            x = -1
            for widget in self.inputs:
                if widget == element:
                    break
                x += 1
            element = self.inputs[x]
            element.delete("1.0", "end")
            element.focus_set()
            self.code[x] = "X"
    
    def getCode(self):
        code = "TECHNO-" + "".join(self.code)
        if len(code) == 32 and code.replace("-", "").isalnum() and code.replace("-", "").isupper():
            return code
        else:
            return "TECHNO-XXXXXXXXXXXXXXXXXXXXXXXXX"

    def confirm(self):
        if self.accepted:
            code = self.getCode()
            # Check code validity