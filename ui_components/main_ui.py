import tkinter as tk
from tkinter import ttk
from .custom_buttons import CustomButton1, gray, white, color2, color3

class MainUI:
    def __init__(self, root, file_handler):
        self.root = root
        self.file_handler = file_handler
        self.setup_main_ui()

    def setup_main_ui(self):
        self.root.title("PicMagic")
        self.root.state('zoomed') 
        self.root.config(bg=gray)

        # Style for the notebook and tabs
        style = ttk.Style()
        style.theme_use('default')

        style.configure('TNotebook', background=gray, borderwidth=0)
        style.configure('TNotebook.Tab', background=color2, foreground=white, font=('Arial', 11, 'bold'), anchor='center', justify='center', padding=[4, 5], bd=0, width=10)
        style.map('TNotebook.Tab', background=[('selected', color3)])

        # Notebook for the sidebar
        self.sidebar = ttk.Notebook(self.root)
        self.sidebar.pack(side=tk.LEFT, fill='y')

        # Frame for upload and delete buttons
        btn_frame1 = tk.Frame(self.root, bg=gray)
        btn_frame1.pack(side=tk.TOP, pady=10)

        # Upload image button
        upload_btn = CustomButton1(btn_frame1, text="Upload image", command=self.file_handler.upload_image)
        upload_btn.grid(row=0, column=0, padx=5)

        # Delete image button
        delete_btn = CustomButton1(btn_frame1, text="Delete image", command=self.file_handler.delete_image)
        delete_btn.grid(row=0, column=1, padx=5)

        # Save image button
        save_btn = CustomButton1(self.root, text="Save image", command=self.file_handler.save_image)
        save_btn.pack(side=tk.BOTTOM, pady=15, padx=(0, 15), anchor="se")

        """ Canvas for Display Images """
        # Display area for images
        img_frame = tk.Frame(self.root)
        img_frame.pack(side=tk.TOP, padx=10)

        self.file_handler.img_canvas1 = tk.Canvas(img_frame, width=610, height=630, bg=white, bd=0, highlightthickness=3, highlightbackground=gray)
        self.file_handler.img_canvas1.pack(side=tk.LEFT)

        self.file_handler.img_canvas2 = tk.Canvas(img_frame, width=610, height=630, bg=white, bd=0, highlightthickness=3, highlightbackground=gray)
        self.file_handler.img_canvas2.pack(side=tk.RIGHT)