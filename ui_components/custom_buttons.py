import customtkinter as ctk

# Define the color palette
black = 'BLACK'
white = 'WHITE'
yellow = '#FFEB3B'
dYellow = '#FFC100'
pink = '#e91e63'

dGray = '#2f2f2f'
lGray = '#989898'

# Custom Button Design
class CustomButton1(ctk.CTkButton):
    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command)
        self.configure(
            fg_color=pink,
            text_color=white,
            corner_radius=20,
            width=150,
            height=40,
            font=('Arial', 17, 'bold'),
            border_width=0
        )

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.configure(fg_color="transparent", border_color=pink, border_width=3) 
    def on_leave(self, event):
        self.configure(fg_color=pink, border_width=0)

class CustomButton2(ctk.CTkButton):
    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command)
        self.configure(
            fg_color=dYellow,
            text_color=black,
            hover_color=yellow,
            corner_radius=20,
            width=150,
            height=35,
            font=('Arial', 15, 'bold')
        ) 

class CustomButton3(ctk.CTkButton):
    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command)
        self.configure(
            fg_color="transparent", 
            border_color=dYellow, 
            border_width=3,
            hover_color=dYellow,
            text_color=white,
            corner_radius=20,
            width=80,
            height=40,
            font=('Arial', 16, 'bold')
        )