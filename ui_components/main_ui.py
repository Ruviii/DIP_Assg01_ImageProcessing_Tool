import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import CTkImage
from .custom_buttons import CustomButton1,CustomButton2, color_2, white, color_3, color_1, black, color_6, color_7,color_12

class MainUI:
    def __init__(self, root, file_handler):
        self.root = root
        self.file_handler = file_handler
        self.setup_main_ui()

    def load_icon(self, image_path, size=(16, 16)):
        image = Image.open(image_path)
        image = image.resize(size, Image.LANCZOS)
        return CTkImage(light_image=image, dark_image=image)

    def setup_main_ui(self):
        self.root.title("PicMagic")
        self.root.state('zoomed') 
        self.root.config(bg=color_1)

        # Style for the notebook and tabs
        style = ttk.Style()
        style.theme_use('default')

        style.configure('TNotebook', background=color_2, borderwidth=0)
        style.configure('TNotebook.Tab', background=color_3, foreground=white, font=('Arial', 11, 'bold'), anchor='center', justify='center', padding=[5, 5], bd=0, width=10)
        style.map('TNotebook.Tab', background=[('selected', color_12)])

        # Notebook for the sidebar
        self.sidebar = ttk.Notebook(self.root)
        self.sidebar.pack(side=tk.LEFT, fill='y')

        # Frame for upload, delete, undo, and redo buttons
        btn_frame1 = tk.Frame(self.root, bg=color_1)
        btn_frame1.pack(side=tk.TOP, fill='x',padx=15, pady=20)

         # Frame for the upload button (left corner)
        left_frame = tk.Frame(btn_frame1, bg=color_1)
        left_frame.pack(side=tk.LEFT, padx=5)

        # Frame for the undo, redo, and delete buttons (right corner)
        right_frame = tk.Frame(btn_frame1, bg=color_1)
        right_frame.pack(side=tk.RIGHT, padx=5)

        # Load default icons
        upload_icon = self.load_icon('assets/upload.png')
        undo_icon = self.load_icon('assets/undo.png')
        redo_icon = self.load_icon('assets/redo.png')
        delete_icon = self.load_icon('assets/delete.png')
        save_icon = self.load_icon('assets/save.png')

        # Load hover icons
        upload_icon_hover = self.load_icon('assets/upload2.png')
        undo_icon_hover = self.load_icon('assets/undo2.png')
        redo_icon_hover = self.load_icon('assets/redo2.png')
        delete_icon_hover = self.load_icon('assets/delete2.png')
        save_icon_hover = self.load_icon('assets/save2.png')

        # Upload image button
        upload_btn = CustomButton1(left_frame, text="Upload image", image=upload_icon, command=self.file_handler.upload_image)
        upload_btn.pack(side=tk.LEFT, padx=5)
        upload_btn.bind("<Enter>", lambda e: upload_btn.configure(image=upload_icon_hover))
        upload_btn.bind("<Leave>", lambda e: upload_btn.configure(image=upload_icon))

        # Undo button
        undo_btn = CustomButton2(right_frame, text="Undo", image=undo_icon, command=self.file_handler.undo_action)
        undo_btn.pack(side=tk.LEFT, padx=5)
        undo_btn.bind("<Enter>", lambda e: undo_btn.configure(image=undo_icon_hover))
        undo_btn.bind("<Leave>", lambda e: undo_btn.configure(image=undo_icon))

        # Redo button
        redo_btn = CustomButton2(right_frame, text="Redo", image=redo_icon, command=self.file_handler.redo_action)
        redo_btn.pack(side=tk.LEFT, padx=(5, 20))
        redo_btn.bind("<Enter>", lambda e: redo_btn.configure(image=redo_icon_hover))
        redo_btn.bind("<Leave>", lambda e: redo_btn.configure(image=redo_icon))

        # Delete image button
        delete_btn = CustomButton1(right_frame, text="Delete image", image=delete_icon, command=self.file_handler.delete_image)
        delete_btn.pack(side=tk.LEFT, padx=5)
        delete_btn.bind("<Enter>", lambda e: delete_btn.configure(image=delete_icon_hover))
        delete_btn.bind("<Leave>", lambda e: delete_btn.configure(image=delete_icon))

        # Save image button
        save_btn = CustomButton1(self.root, text="Save image", image=save_icon, command=self.file_handler.save_image)
        save_btn.pack(side=tk.BOTTOM, pady=20, padx=(0, 20), anchor="se")
        save_btn.bind("<Enter>", lambda e: save_btn.configure(image=save_icon_hover))
        save_btn.bind("<Leave>", lambda e: save_btn.configure(image=save_icon))

        """ Canvas for Display Images """
        # Display area for images
        img_frame = tk.Frame(self.root)
        img_frame.pack(side=tk.TOP, padx=10)

        self.file_handler.img_canvas1 = tk.Canvas(img_frame, width=610, height=630, bg=white, bd=0, highlightthickness=4, highlightbackground=color_6)
        self.file_handler.img_canvas1.pack(side=tk.LEFT)

        self.file_handler.img_canvas2 = tk.Canvas(img_frame, width=610, height=630, bg=white, bd=0, highlightthickness=4, highlightbackground=color_6)
        self.file_handler.img_canvas2.pack(side=tk.RIGHT)