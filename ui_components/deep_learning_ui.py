import tkinter as tk
import customtkinter as ctk
from .custom_buttons import CustomButton3,CustomButton4,color_10, color_3, white, lGray, black, color_5, color_8, color_2

class DeepLearningUI:
    def __init__(self, sidebar, style_transfer, ai_image_segmentation):
        self.sidebar = sidebar
        self.style_transfer = style_transfer
        self.ai_image_segmentation = ai_image_segmentation
        self.setup_deep_learning_ui()

    def setup_deep_learning_ui(self):
        tab3 = ctk.CTkFrame(self.sidebar, fg_color=color_2)
        self.sidebar.add(tab3, text="AI Tools")

        # Create a scrollable frame
        s_frame = ctk.CTkScrollableFrame(tab3, width=200, height=200, fg_color=color_2)
        s_frame.pack(padx=(5,0), fill="both", expand=True)

        s_frame._scrollbar.configure(
            button_color=lGray,
            button_hover_color= color_3 
        )

        # Create frames for  style_transfer and ai_image_segmentation
    
        style_transfer_frame = ctk.CTkFrame(s_frame, fg_color="transparent", corner_radius=20, border_width=3, border_color=color_8)
        style_transfer_frame.grid(row=1, column=0, padx=20, pady=10)

        ai_image_segmentation_frame = ctk.CTkFrame(s_frame, fg_color="transparent", corner_radius=20, border_width=3, border_color=color_10)
        ai_image_segmentation_frame.grid(row=3, column=0, padx=20, pady=10)

        # Add titles above each frame
        
        style_transfer_label = tk.Label(s_frame, text="Style Transfer", bg=color_2, fg=black, font=('Arial', 16, 'bold'))
        style_transfer_label.grid(row=0, column=0, padx=5, pady=(10, 0), sticky="w")

        ai_image_segmentation_label = tk.Label(s_frame, text="AI Image Segmentation", bg=color_2, fg=black, font=('Arial', 16, 'bold'))
        ai_image_segmentation_label.grid(row=2, column=0, padx=5, pady=(10, 0), sticky="w")


    #----------buttons for ai_image_segmentation----------#

        apply_segmentation_button = CustomButton4(ai_image_segmentation_frame, text="Apply Segmentation", command=self.ai_image_segmentation.apply_segmentation)
        apply_segmentation_button.pack(padx=10, pady=(25,25))

    #----------buttons for style_transfer----------#

        upload_style_button = CustomButton3(style_transfer_frame, text="Upload Style", command=self.style_transfer.upload_style_image)
        upload_style_button.pack(padx=10, pady=(25,10))

        self.style_image_label = tk.Label(style_transfer_frame, text="No image uploaded", bg=color_2, fg=black)
        self.style_image_label.pack(padx=10, pady=10)

        delete_style_btn = CustomButton3(style_transfer_frame, text="Delete Style", command=self.style_transfer.delete_style_image)
        delete_style_btn.pack(padx=10, pady=10)

        apply_style_button = CustomButton3(style_transfer_frame, text="Apply Style", command=self.style_transfer.apply_style_transfer)
        apply_style_button.pack(padx=10, pady=(10,25))

        # Pass the style_image_label to the style_transfer instance
        self.style_transfer.set_style_image_label(self.style_image_label)