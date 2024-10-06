import customtkinter as ctk
import tkinter as tk
from .custom_buttons import CustomButton5,CustomButton3,CustomButton4, color_2, lGray,color_3,color_4,white,color_5,color_12,black,color_7,color_9

class BasicUI:
    def __init__(self, sidebar, basic_processor):
        self.sidebar = sidebar
        self.basic_processor = basic_processor
        self.setup_basic_ui()

    def setup_basic_ui(self):
        tab1 = ctk.CTkFrame(self.sidebar, fg_color=color_2)
        self.sidebar.add(tab1, text="Basics")

        # Create a scrollable frame
        scrollable_frame = ctk.CTkScrollableFrame(tab1, width=200, height=200, fg_color=color_2)
        scrollable_frame.pack(padx=(5,0), fill="both", expand=True)

        scrollable_frame._scrollbar.configure(
            button_color=lGray,
            button_hover_color= color_3 
        )

        btn_frame3 = ctk.CTkFrame(scrollable_frame, fg_color="transparent", corner_radius=20, border_width=3, border_color=color_12)
        btn_frame3.pack(side=ctk.TOP,padx=20,pady=15)

        rotate_btn = CustomButton5(btn_frame3, text="Rotate", command=self.basic_processor.rotate_image)
        rotate_btn.pack(pady=(25,10), padx=20)

        crop_btn = CustomButton5(btn_frame3, text="Crop", command=self.basic_processor.crop_image)
        crop_btn.pack(pady=10, padx=20)

        flip_btn = CustomButton5(btn_frame3, text="Flip", command=self.basic_processor.flip_image)
        flip_btn.pack(pady=10, padx=20)

        brightness_btn = CustomButton5(btn_frame3, text="Brightness", command=self.basic_processor.change_brightness)
        brightness_btn.pack(pady=(10,25), padx=20)

        # Buttons to draw shapes and lines on the image
        btn_frame2 = ctk.CTkFrame(scrollable_frame, fg_color="transparent", corner_radius=20, border_width=3, border_color=color_7)
        btn_frame2.pack(side=ctk.TOP,padx=20,pady=15)

        slider_label = tk.Label(btn_frame2, text="Adjust Line Thicknes", bg=color_2, fg=black, font=('Arial', 11, 'bold'))
        slider_label.pack(padx=10, pady=(25, 0))

        thickness_slider = ctk.CTkSlider(btn_frame2, from_=1, to=100, orientation='horizontal', width=200,fg_color=color_12, progress_color=color_3, button_color=color_7,button_hover_color= color_9, command=self.basic_processor.update_thickness)
        thickness_slider.set(self.basic_processor.line_thickness)
        thickness_slider.pack(pady=10, padx=20)

        draw_line_btn = CustomButton3(btn_frame2, text="Draw Line", command=self.basic_processor.drawing_line)
        draw_line_btn.pack(pady=10, padx=20)

        draw_circle_btn = CustomButton3(btn_frame2, text="Draw Circle", command=self.basic_processor.drawing_circle)
        draw_circle_btn.pack(pady=10, padx=20)

        draw_rectangle_btn = CustomButton3(btn_frame2, text="Draw Rectangle", command=self.basic_processor.drawing_rectangle)
        draw_rectangle_btn.pack(pady=10, padx=20)

        draw_triangle_btn = CustomButton3(btn_frame2, text="Draw Triangle", command=self.basic_processor.drawing_triangle)
        draw_triangle_btn.pack(pady=10, padx=20)

        draw_square_btn = CustomButton3(btn_frame2, text="Draw Square", command=self.basic_processor.drawing_square)
        draw_square_btn.pack(pady=(10, 25), padx=20)

        btn_frame4 = ctk.CTkFrame(scrollable_frame, fg_color="transparent", corner_radius=20, border_width=3, border_color=color_3)
        btn_frame4.pack(side=ctk.TOP,padx=20,pady=15)

        sample_btn = CustomButton4(btn_frame4, text="Test Button", command=self.basic_processor.drawing_square)
        sample_btn.pack(pady=(10, 25), padx=20)
        
        sample_btn = CustomButton4(btn_frame4, text="Test Button", command=self.basic_processor.drawing_square)
        sample_btn.pack(pady=(10, 25), padx=20)
