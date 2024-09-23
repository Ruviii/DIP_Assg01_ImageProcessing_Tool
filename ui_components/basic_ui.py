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

        # Get the screen height
        screen_height = self.sidebar.winfo_screenheight()

        # Create a canvas and a scrollbar
        canvas = tk.Canvas(tab1, bg=dGray, bd=0, highlightthickness=0,width=200,height=screen_height)
        scrollbar = tk.Scrollbar(tab1, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=dGray)

        # Bind the configuration of the scrollable frame to update the canvas scroll region
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        # Create a window in the canvas to hold the scrollable frame
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack the canvas and scrollbar
        canvas.pack(side=tk.LEFT,padx=25)
        scrollbar.pack(side="right", fill="y")

        undo_btn = CustomButton2(scrollable_frame, text="Undo", command=self.basic_processor.undo_action)
        undo_btn.pack(pady=10)

        redo_btn = CustomButton2(scrollable_frame, text="Redo", command=self.basic_processor.redo_action)
        redo_btn.pack(pady=10)

        rotate_btn = CustomButton2(scrollable_frame, text="Rotate", command=self.basic_processor.rotate_image)
        rotate_btn.pack(pady=10)

        crop_btn = CustomButton2(scrollable_frame, text="Crop", command=self.basic_processor.crop_image)
        crop_btn.pack(pady=10)

        flip_btn = CustomButton2(scrollable_frame, text="Flip", command=self.basic_processor.flip_image)
        flip_btn.pack(pady=10)

        brightness_btn = CustomButton2(scrollable_frame, text="Brightness", command=self.basic_processor.change_brightness)
        brightness_btn.pack(pady=10)

        btn_frame2 = tk.Frame(scrollable_frame, bg=lGray)
        btn_frame2.pack(side=tk.TOP, pady=20)

        thickness_slider = tk.Scale(scrollable_frame, from_=1, to=100, orient='horizontal', length=200, label="Line Thickness", command=self.basic_processor.update_thickness)
        thickness_slider.set(self.basic_processor.line_thickness)
        thickness_slider.pack(pady=10)

        draw_line_btn = CustomButton2(scrollable_frame, text="Draw Line", command=self.basic_processor.drawing_line)
        draw_line_btn.pack(pady=10)

        draw_circle_btn = CustomButton2(scrollable_frame, text="Draw Circle", command=self.basic_processor.drawing_circle)
        draw_circle_btn.pack(pady=10)

        draw_rectangle_btn = CustomButton2(scrollable_frame, text="Draw Rectangle", command=self.basic_processor.drawing_rectangle)
        draw_rectangle_btn.pack(pady=10)

        draw_triangle_btn = CustomButton2(scrollable_frame, text="Draw Triangle", command=self.basic_processor.drawing_triangle)
        draw_triangle_btn.pack(pady=10)

        draw_square_btn = CustomButton2(scrollable_frame, text="Draw Square", command=self.basic_processor.drawing_square)
        draw_square_btn.pack(pady=10)
