import tkinter as tk

gray = '#676767'
dGray = '#4C4C4C'
lGray = '#989898'
black = 'BLACK'
white = 'WHITE'
color1 = '#020f12'
color2 = '#0387E7'
color3 = '#05C3FF'

# Custom Button Design
class CustomButton1(tk.Button):
    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command)
        self.configure(
            background=color2,
            foreground=white,
            padx=15,
            activebackground=color3,
            activeforeground=white,
            width=10,
            height=1,
            relief='raised',
            border=5, 
            cursor='hand2',
            font=('Arial', 16, 'bold')
        )

class CustomButton2(tk.Button):
    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command)
        self.configure(
            background=gray,
            foreground=white,
            padx=15,
            activebackground=gray,
            activeforeground=color2,
            width=10,
            height=1,
            border=4,
            relief='groove',
            cursor='hand2',
            font=('Arial', 13, 'bold')
        ) 
