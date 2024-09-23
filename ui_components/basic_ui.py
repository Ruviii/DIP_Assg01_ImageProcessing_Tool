import tkinter as tk
from .custom_buttons import CustomButton2, dGray, lGray

class BasicUI:
    def __init__(self, sidebar, basic_processor):
        self.sidebar = sidebar
        self.basic_processor = basic_processor
        self.setup_basic_ui()

    def setup_basic_ui(self):
        tab1 = tk.Frame(self.sidebar, bg=dGray, bd=0)
        self.sidebar.add(tab1, text="Basics")

        # Rotate button
        rotate_btn = CustomButton2(tab1, text="Rotate", command=self.basic_processor.rotate_image)
        rotate_btn.pack(pady=10)

        # Crop button
        crop_btn = CustomButton2(tab1, text="Crop", command=self.basic_processor.crop_image)
        crop_btn.pack(pady=10)

        # Flip button
        flip_btn = CustomButton2(tab1, text="Flip", command=self.basic_processor.flip_image)
        flip_btn.pack(pady=10)

        # Change Brightness button
        brightness_btn = CustomButton2(tab1, text="Brightness", command=self.basic_processor.change_brightness)
        brightness_btn.pack(pady=10)

        # Undo button
        undo_btn = CustomButton2(tab1, text="Undo", command=self.basic_processor.undo_action)
        undo_btn.pack(pady=10)

        # Redo button
        redo_btn = CustomButton2(tab1, text="Redo", command=self.basic_processor.redo_action)
        redo_btn.pack(pady=10)

        # Frame for shape drawing buttons
        btn_frame2 = tk.Frame(tab1, bg=lGray)
        btn_frame2.pack(side=tk.TOP, pady=20)

        # Add the line thickness slider in the Basic tab
        thickness_slider = tk.Scale(tab1, from_=1, to=100, orient='horizontal', length=200, label="Line Thickness", command=self.basic_processor.update_thickness)
        thickness_slider.set(self.basic_processor.line_thickness)  # Set the initial thickness
        thickness_slider.pack(pady=10)

        # Draw Line button
        draw_line_btn = CustomButton2(tab1, text="Draw Line", command=self.basic_processor.drawing_line)
        draw_line_btn.pack(pady=10)

        # Draw Circle button
        draw_circle_btn = CustomButton2(tab1, text="Draw Circle", command=self.basic_processor.drawing_circle)
        draw_circle_btn.pack(pady=10)

        # Draw Rectangle button
        draw_rectangle_btn = CustomButton2(tab1, text="Draw Rectangle", command=self.basic_processor.drawing_rectangle)
        draw_rectangle_btn.pack(pady=10)

        # Draw Triangle button
        draw_triangle_btn = CustomButton2(tab1, text="Draw Triangle", command=self.basic_processor.drawing_triangle)
        draw_triangle_btn.pack(pady=10)

        # Draw Square button
        draw_square_btn = CustomButton2(tab1, text="Draw Square", command=self.basic_processor.drawing_square)
        draw_square_btn.pack(pady=10)