import cv2
import numpy as np
from PIL import Image, ImageEnhance
import tkinter as tk
from utils.file_handler import FileHandler

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

    def undo_action(self):
        self.file_handler.undo_action()

    def redo_action(self):
        self.file_handler.redo_action()