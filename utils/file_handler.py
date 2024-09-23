import cv2
from tkinter import filedialog
from PIL import Image, ImageTk


class FileHandler:
    def __init__(self):
        self.original_img = None
        self.processed_img = None
        self.img_path = None
        self.img_canvas1 = None
        self.img_canvas2 = None
        self.undo_stack = []
        self.redo_stack = []

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_img = cv2.imread(file_path)
            self.img_path = file_path
            self.processed_img = self.original_img.copy()
            self.display_image(self.original_img, self.img_canvas1)
            self.display_image(self.processed_img, self.img_canvas2)

    def delete_image(self):
        if self.img_canvas1 and self.img_canvas2:
            self.img_canvas1.delete("all")
            self.img_canvas2.delete("all")

    def display_image(self, img, canvas):
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_pil.thumbnail((canvas_width, canvas_height), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(image=img_pil)
        canvas.delete("all")
        canvas.create_image(0, 0, anchor='nw', image=img_tk)
        canvas.image = img_tk

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file_path:
            cv2.imwrite(file_path, self.processed_img)

    def save_undo_state(self):
        if self.processed_img is not None:
            self.undo_stack.append(self.processed_img.copy())
            self.redo_stack.clear()  # Clear redo stack when new action is performed

    def undo_action(self):
        if self.undo_stack:
            self.redo_stack.append(self.processed_img.copy())
            self.processed_img = self.undo_stack.pop()
            self.display_image(self.processed_img, self.img_canvas2)

    def redo_action(self):
        if self.redo_stack:
            self.undo_stack.append(self.processed_img.copy())
            self.processed_img = self.redo_stack.pop()
            self.display_image(self.processed_img, self.img_canvas2)