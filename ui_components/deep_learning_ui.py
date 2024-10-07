import tkinter as tk
import customtkinter as ctk
from .custom_buttons import CustomButton3,CustomButton4,CustomButton5, color_10, color_3, white, lGray, black, color_5, color_8, color_2

class DeepLearningUI:
    def __init__(self, sidebar, style_transfer, image_enhancement, image_generator, ai_image_segmentation):
        self.sidebar = sidebar
        self.style_transfer = style_transfer
        self.image_enhancement = image_enhancement
        self.image_generator = image_generator
        self.ai_image_segmentation = ai_image_segmentation
        self.setup_deep_learning_ui()

    def setup_deep_learning_ui(self):
        tab3 = tk.Frame(self.sidebar, bg=color_2, bd=0)
        self.sidebar.add(tab3, text="AI Tools")

        # Create a scrollable frame
        s_frame = ctk.CTkScrollableFrame(tab3, width=200, height=200, fg_color=color_2)
        s_frame.pack(padx=(5,0), fill="both", expand=True)

        s_frame._scrollbar.configure(
            button_color=lGray,
            button_hover_color= color_3 
        )

        # Create frames for  
        ai_image_segmentation_frame = ctk.CTkFrame(s_frame, fg_color="transparent", corner_radius=20, border_width=3, border_color=color_10)
        ai_image_segmentation_frame.grid(row=1, column=0, padx=10, pady=10)

        image_enhancement_frame = ctk.CTkFrame(s_frame, fg_color="transparent", corner_radius=20, border_width=3, border_color=color_3)
        image_enhancement_frame.grid(row=3, column=0, padx=10, pady=10)

        image_genaration_frame = ctk.CTkFrame(s_frame, fg_color="transparent", corner_radius=20, border_width=3, border_color=color_5)
        image_genaration_frame.grid(row=5, column=0, padx=10, pady=10)

        style_transfer_frame = ctk.CTkFrame(s_frame, fg_color="transparent", corner_radius=20, border_width=3, border_color=color_8)
        style_transfer_frame.grid(row=7, column=0, padx=10, pady=10)

        # Add titles above each frame
        ai_image_segmentation_label = tk.Label(s_frame, text="AI Image Segmentation", bg=color_2, fg=black, font=('Arial', 16, 'bold'))
        ai_image_segmentation_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        image_enhancement_label = tk.Label(s_frame, text="Image Enhancement", bg=color_2, fg=black, font=('Arial', 16, 'bold'))
        image_enhancement_label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

        image_segmentation_label = tk.Label(s_frame, text="Image Genaration", bg=color_2, fg=black, font=('Arial', 16, 'bold'))
        image_segmentation_label.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")

        style_transfer_label = tk.Label(s_frame, text="Style Transfer", bg=color_2, fg=black, font=('Arial', 16, 'bold'))
        style_transfer_label.grid(row=6, column=0, padx=10, pady=(10, 0), sticky="w")

    #----------buttons for ai_image_segmentation----------#

    #----------buttons for image_enhancement----------#

    #----------buttons for image_generator----------#

    #----------buttons for style_transfer----------#