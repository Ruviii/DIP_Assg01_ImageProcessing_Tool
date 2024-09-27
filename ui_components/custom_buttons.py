import customtkinter as ctk

# Define the color palette
black = 'BLACK'
white = 'WHITE'

color_1= '#F5F5F5' #background color
color_2 = 'WHITE' #sidebar color

color_3 = '#5C2FC2' #common buttons color

color_4 = '#FFC700' #button color 3.1 
color_5 = '#FFDB00' #button color 3.2

color_8 = '#FF0080' #button color 4.1
color_9 = '#FF4191' #button color 4.2

color_10 = '#FF6600' #button color 5.1
color_11 = '#FF885B' #button color 5.2

color_6 = '#c7defa' #canvas border color
color_7 = '#FF0080' #undo redo button color

color_12 = '#7B66FF'
lGray = '#989898'


# Custom Button Design
class CustomButton1(ctk.CTkButton):             # File handling buttons
    def __init__(self, parent, text, command, image=None):
        super().__init__(parent, text=text, command=command, image=image, compound="left")
        self.configure(
            fg_color=color_3,
            text_color=white,
            corner_radius=20,
            width=160,
            height=40,
            font=('Arial', 17, 'bold'),
            border_width=0
        )

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.configure(fg_color="transparent", border_color=color_3, border_width=4,text_color=color_3) 
    def on_leave(self, event):
        self.configure(fg_color=color_3, border_width=0, text_color=white)

class CustomButton2(ctk.CTkButton):            # Undo, Redo buttons
    def __init__(self, parent, text, command, image=None):
        super().__init__(parent, text=text, command=command, image=image, compound="left")
        self.configure(
            fg_color=color_7,
            text_color=white,
            corner_radius=20,
            width=80,
            height=40,
            font=('Arial', 17, 'bold'),
            border_width=0
        )

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.configure(fg_color="transparent", border_color=color_7, border_width=4,text_color=color_7) 
    def on_leave(self, event):
        self.configure(fg_color=color_7, border_width=0, text_color=white)
 
class CustomButton3(ctk.CTkButton):           # Ruvini
    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command)
        self.configure(
            fg_color=color_4,
            text_color=black,
            hover_color=color_5,
            corner_radius=20,
            width=200,
            height=35,
            font=('Arial', 15, 'bold')
        ) 

class CustomButton4(ctk.CTkButton):         # Dulmini
    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command)
        self.configure(
            fg_color=color_8,
            text_color=black,
            hover_color=color_9,
            corner_radius=20,
            width=200,
            height=35,
            font=('Arial', 15, 'bold')
        )

class CustomButton5(ctk.CTkButton):        # Hasara
    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command)
        self.configure(
            fg_color=color_10,
            text_color=black,
            hover_color=color_11,
            corner_radius=20,
            width=200,
            height=35,
            font=('Arial', 15, 'bold')
        )