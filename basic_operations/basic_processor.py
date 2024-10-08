import cv2
import numpy as np
from PIL import Image, ImageEnhance
import tkinter as tk
from utils.file_handler import FileHandler
from tkinter import simpledialog
from tkinter.colorchooser import askcolor

class BasicProcessor:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.line_thickness = 1
        self.drawing = False
        self.ix, self.iy = -1, -1

    def rotate_image(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            # Convert OpenCV (numpy) image to Pillow
            img_pil = Image.fromarray(cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2RGB))
            img_pil = img_pil.rotate(45)
            # Convert back to OpenCV (numpy) format
            self.file_handler.processed_img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def crop_image(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            # Convert OpenCV (numpy) image to Pillow
            img_pil = Image.fromarray(cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2RGB))
            img_pil = img_pil.crop((100, 100, 400, 400))
            # Convert back to OpenCV (numpy) format
            self.file_handler.processed_img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def flip_image(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            # Convert OpenCV (numpy) image to Pillow
            img_pil = Image.fromarray(cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2RGB))
            img_pil = img_pil.transpose(Image.FLIP_LEFT_RIGHT)
            # Convert back to OpenCV (numpy) format
            self.file_handler.processed_img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def change_brightness(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            # Convert OpenCV (numpy) image to Pillow
            img_pil = Image.fromarray(cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2RGB))
            enhancer = ImageEnhance.Brightness(img_pil)
            img_pil = enhancer.enhance(1.5)  # Increase brightness by 50%
            # Convert back to OpenCV (numpy) format
            self.file_handler.processed_img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Functions to draw shapes and Lines on the image
    def update_thickness(self, value):
        self.line_thickness = int(value)

    def draw_line(self, event):
        x, y = event.x, event.y
        if event.type == tk.EventType.ButtonPress:
            self.file_handler.save_undo_state()
            self.drawing = True
            self.ix, self.iy = x, y
        elif event.type == tk.EventType.Motion:
            if self.drawing:
                temp_img = self.file_handler.processed_img.copy()
                cv2.line(temp_img, (self.ix, self.iy), (x, y), (0, 200, 255), thickness=self.line_thickness)
                self.file_handler.display_image(temp_img, self.file_handler.img_canvas2)
        elif event.type == tk.EventType.ButtonRelease:
            self.drawing = False
            cv2.line(self.file_handler.processed_img, (self.ix, self.iy), (x, y), (0, 200, 255), thickness=self.line_thickness)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def drawing_line(self):
        self.file_handler.img_canvas2.bind("<ButtonPress-1>", self.draw_line)
        self.file_handler.img_canvas2.bind("<B1-Motion>", self.draw_line)
        self.file_handler.img_canvas2.bind("<ButtonRelease-1>", self.draw_line)

    def draw_circle(self, event):
        x, y = event.x, event.y
        if event.type == tk.EventType.ButtonPress:
            self.file_handler.save_undo_state()
            self.drawing = True
            self.ix, self.iy = x, y
        elif event.type == tk.EventType.Motion:
            if self.drawing:
                temp_img = self.file_handler.processed_img.copy()
                radius = int(((x - self.ix) ** 2 + (y - self.iy) ** 2) ** 0.5)
                cv2.circle(temp_img, (self.ix, self.iy), radius, (0, 200, 255), thickness=self.line_thickness)
                self.file_handler.display_image(temp_img, self.file_handler.img_canvas2)
        elif event.type == tk.EventType.ButtonRelease:
            self.drawing = False
            radius = int(((x - self.ix) ** 2 + (y - self.iy) ** 2) ** 0.5)
            cv2.circle(self.file_handler.processed_img, (self.ix, self.iy), radius, (0, 200, 255), thickness=self.line_thickness)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def drawing_circle(self):
        self.file_handler.img_canvas2.bind("<ButtonPress-1>", self.draw_circle)
        self.file_handler.img_canvas2.bind("<B1-Motion>", self.draw_circle)
        self.file_handler.img_canvas2.bind("<ButtonRelease-1>", self.draw_circle)

    def draw_rectangle(self, event):
        x, y = event.x, event.y
        if event.type == tk.EventType.ButtonPress:
            self.file_handler.save_undo_state()
            self.drawing = True
            self.ix, self.iy = x, y
        elif event.type == tk.EventType.Motion:
            if self.drawing:
                temp_img = self.file_handler.processed_img.copy()
                cv2.rectangle(temp_img, (self.ix, self.iy), (x, y), (0, 200, 255), thickness=self.line_thickness)
                self.file_handler.display_image(temp_img, self.file_handler.img_canvas2)
        elif event.type == tk.EventType.ButtonRelease:
            self.drawing = False
            cv2.rectangle(self.file_handler.processed_img, (self.ix, self.iy), (x, y), (0, 200, 255), thickness=self.line_thickness)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def drawing_rectangle(self):
        self.file_handler.img_canvas2.bind("<ButtonPress-1>", self.draw_rectangle)
        self.file_handler.img_canvas2.bind("<B1-Motion>", self.draw_rectangle)
        self.file_handler.img_canvas2.bind("<ButtonRelease-1>", self.draw_rectangle)

    def draw_triangle(self, event):
        x, y = event.x, event.y
        if event.type == tk.EventType.ButtonPress:
            self.file_handler.save_undo_state()
            self.drawing = True
            self.ix, self.iy = x, y
        elif event.type == tk.EventType.Motion:
            if self.drawing:
                temp_img = self.file_handler.processed_img.copy()
                points = np.array([[self.ix, self.iy], [x, y], [(self.ix + x) // 2, self.iy - (y - self.iy)]], np.int32)
                cv2.polylines(temp_img, [points], isClosed=True, color=(0, 200, 255), thickness=self.line_thickness)
                self.file_handler.display_image(temp_img, self.file_handler.img_canvas2)
        elif event.type == tk.EventType.ButtonRelease:
            self.drawing = False
            points = np.array([[self.ix, self.iy], [x, y], [(self.ix + x) // 2, self.iy - (y - self.iy)]], np.int32)
            cv2.polylines(self.file_handler.processed_img, [points], isClosed=True, color=(0, 200, 255), thickness=self.line_thickness)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def drawing_triangle(self):
        self.file_handler.img_canvas2.bind("<ButtonPress-1>", self.draw_triangle)
        self.file_handler.img_canvas2.bind("<B1-Motion>", self.draw_triangle)
        self.file_handler.img_canvas2.bind("<ButtonRelease-1>", self.draw_triangle)

    def draw_square(self, event):
        x, y = event.x, event.y
        if event.type == tk.EventType.ButtonPress:
            self.file_handler.save_undo_state()
            self.drawing = True
            self.ix, self.iy = x, y
        elif event.type == tk.EventType.Motion:
            if self.drawing:
                temp_img = self.file_handler.processed_img.copy()
                side_length = min(abs(x - self.ix), abs(y - self.iy))
                cv2.rectangle(temp_img, (self.ix, self.iy), (self.ix + side_length, self.iy + side_length), (0, 200, 255), thickness=self.line_thickness)
                self.file_handler.display_image(temp_img, self.file_handler.img_canvas2)
        elif event.type == tk.EventType.ButtonRelease:
            self.drawing = False
            side_length = min(abs(x - self.ix), abs(y - self.iy))
            cv2.rectangle(self.file_handler.processed_img, (self.ix, self.iy), (self.ix + side_length, self.iy + side_length), (0, 200, 255), thickness=self.line_thickness)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def drawing_square(self):
        self.file_handler.img_canvas2.bind("<ButtonPress-1>", self.draw_square)
        self.file_handler.img_canvas2.bind("<B1-Motion>", self.draw_square)
        self.file_handler.img_canvas2.bind("<ButtonRelease-1>", self.draw_square)

    # Functions to Dulmini

    def convert_to_grayscale(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            self.file_handler.processed_img = cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2GRAY)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def convert_to_black_and_white(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            gray_img = cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2GRAY)
            _, bw_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
            self.file_handler.processed_img = bw_img
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def convert_to_black_and_white(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
        
            # Check if the image is already grayscale (has 1 channel)
            if len(self.file_handler.processed_img.shape) == 3:
                # Convert to grayscale if the image has 3 channels (BGR)
                gray_img = cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2GRAY)
            else:
                # Image is already grayscale
                gray_img = self.file_handler.processed_img
        
            #Apply threshold to convert grayscale to black and white
            _, bw_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
            self.file_handler.processed_img = bw_img
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)
        

    def convert_to_rgb(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            self.file_handler.processed_img = cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2RGB)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def convert_to_cmyk(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            # Convert OpenCV (numpy) image to Pillow
            img_pil = Image.fromarray(cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2RGB))
            cmyk_img = img_pil.convert('CMYK')
            # Convert back to RGB for display in OpenCV
            rgb_img = cmyk_img.convert('RGB')
            self.file_handler.processed_img = cv2.cvtColor(np.array(rgb_img), cv2.COLOR_RGB2BGR)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def convert_to_hsv(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            self.file_handler.processed_img = cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2HSV)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    

    def add_text_to_image(self):
        if self.file_handler.processed_img is not None:
            # Save the current state for undo before making any modifications
            self.file_handler.save_undo_state()

            def on_ok():
                # Get values from the pop-up
                text = text_entry.get()
                x = int(x_entry.get())
                y = int(y_entry.get())
                font_size = int(size_entry.get())
                color_code = color_entry.get()
                # Convert hex color to BGR for OpenCV
                color_bgr = tuple(int(color_code[i:i+2], 16) for i in (5, 3, 1))  # Convert to (B, G, R)

                # Add the text to the image
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(self.file_handler.processed_img, text, (x, y), font, font_size, color_bgr, 2, cv2.LINE_AA)
                self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)
                dialog_box.destroy()  # Close the dialog after adding text

            # Create a pop-up dialog
            dialog_box = tk.Toplevel()
            dialog_box.title("Add Text to Image")

            # Text input
            tk.Label(dialog_box, text="Text:").grid(row=0, column=0, padx=10, pady=5)
            text_entry = tk.Entry(dialog_box)
            text_entry.grid(row=0, column=1, padx=10, pady=5)

            # X coordinate input
            tk.Label(dialog_box, text="X coordinate:").grid(row=1, column=0, padx=10, pady=5)
            x_entry = tk.Entry(dialog_box)
            x_entry.grid(row=1, column=1, padx=10, pady=5)

            # Y coordinate input
            tk.Label(dialog_box, text="Y coordinate:").grid(row=2, column=0, padx=10, pady=5)
            y_entry = tk.Entry(dialog_box)
            y_entry.grid(row=2, column=1, padx=10, pady=5)

            # Font size input
            tk.Label(dialog_box, text="Font Size:").grid(row=3, column=0, padx=10, pady=5)
            size_entry = tk.Entry(dialog_box)
            size_entry.grid(row=3, column=1, padx=10, pady=5)

            # Color picker
            def pick_color():
                color_code = askcolor(title="Choose Text Color")[1]  # Get hex color
                color_entry.delete(0, tk.END)
                color_entry.insert(0, color_code)

            tk.Label(dialog_box, text="Text Color (Hex):").grid(row=4, column=0, padx=10, pady=5)
            color_entry = tk.Entry(dialog_box)
            color_entry.grid(row=4, column=1, padx=10, pady=5)
            color_button = tk.Button(dialog_box, text="Pick Color", command=pick_color)
            color_button.grid(row=4, column=2, padx=10, pady=5)

            # OK button to add text
            ok_button = tk.Button(dialog_box, text="OK", command=on_ok)
            ok_button.grid(row=5, column=1, padx=10, pady=10)

            dialog_box.mainloop()
 
    def undo_action(self):
        self.file_handler.undo_action()

    def redo_action(self):
        self.file_handler.redo_action()