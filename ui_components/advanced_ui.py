import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from .custom_buttons import CustomButton5, CustomButton4,CustomButton3,color_2, color_3, white, lGray, black, color_5, color_7

class AdvancedUI:
    def __init__(self, sidebar, filter, intensity_manipulation, image_segmentation):
        self.sidebar = sidebar
        self.filter = filter
        self.intensity_manipulation = intensity_manipulation
        self.image_segmentation = image_segmentation
        self.setup_advanced_ui()

    def setup_advanced_ui(self):
        tab2 = tk.Frame(self.sidebar, bg=color_2, bd=0)
        self.sidebar.add(tab2, text="Advanced")

        # Create a scrollable frame
        s_frame = ctk.CTkScrollableFrame(tab2, width=200, height=400, fg_color=color_2)#increase height 200 to 400
        s_frame.pack(padx=(5,0), fill="both", expand=True)

        s_frame._scrollbar.configure(
            button_color=lGray,
            button_hover_color= color_3 
        )

        # Create frames for filters, intensity manipulation, and image segmentation 
        filters_frame = ctk.CTkFrame(s_frame, fg_color="transparent", corner_radius=20, border_width=3, border_color=color_5)
        filters_frame.grid(row=1, column=0, padx=10, pady=10)

        intensity_manipulation_frame = ctk.CTkFrame(s_frame, fg_color="transparent", corner_radius=20, border_width=3, border_color=color_3)
        intensity_manipulation_frame.grid(row=3, column=0, padx=10, pady=10)

        image_segmentation_frame = ctk.CTkFrame(s_frame, fg_color="transparent", corner_radius=20, border_width=3, border_color=color_7)
        image_segmentation_frame.grid(row=5, column=0, padx=10, pady=10)

        # Add titles above each frame
        filters_label = tk.Label(s_frame, text="Filters", bg=color_2, fg=black, font=('Arial', 16, 'bold'))
        filters_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        intensity_manipulation_label = tk.Label(s_frame, text="Intensity Manipulation", bg=color_2, fg=black, font=('Arial', 16, 'bold'))
        intensity_manipulation_label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

        image_segmentation_label = tk.Label(s_frame, text="Image Segmentation", bg=color_2, fg=black, font=('Arial', 16, 'bold'))
        image_segmentation_label.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")

        # -----Add buttons to the Filters tab------

        # Button to apply histogram equalization filter
        histogram_equalization_btn = CustomButton4(filters_frame, text="Apply HistEqualization", command=self.filter.filter_histogram_equalization)
        histogram_equalization_btn.pack(pady=(20,5), padx=10)

        # Button to apply CLAHE filter
        clahe_btn = CustomButton4(filters_frame, text="Apply CLAHE", command=self.filter.filter_clahe)
        clahe_btn.pack(pady=5, padx=10)

        # Button to apply Minimum filter
        min_filter_btn = CustomButton4(filters_frame, text="Minimum Filter", command=self.filter.filter_minimum)
        min_filter_btn.pack(pady=5, padx=10)

        # Button to apply Maximum filter
        max_filter_btn = CustomButton4(filters_frame, text="Maximum Filter", command=self.filter.filter_maximum)
        max_filter_btn.pack(pady=5, padx=10)

        # Button to apply Median filter
        median_filter_btn = CustomButton4(filters_frame, text="Median Filter", command=self.filter.filter_median)
        median_filter_btn.pack(pady=5, padx=10)

        # Button to apply Gaussian Blur filter
        gaussian_blur_btn = CustomButton4(filters_frame, text="Gaussian Blur", command=self.filter.filter_gaussian_blur)
        gaussian_blur_btn.pack(pady=5, padx=10)

        # Button to apply Linear filter
        linear_filter_btn = CustomButton4(filters_frame, text="Apply Linear Filter", command=self.filter.filter_linear)
        linear_filter_btn.pack(pady=(5,20), padx=10)

        # -----Add buttons to the Intensity Manipulation tab------



        # -----Add buttons to the Image Segmentation tab------

        # Button for Thresholding Segmentation
        thresholding_btn = CustomButton5(image_segmentation_frame, text="Apply Thresholding", command=self.image_segmentation.thresholding)
        thresholding_btn.pack(pady=(20,5), padx=10)

        # Button for Edge Detection
        edge_detection_btn = CustomButton5(image_segmentation_frame, text="Edge Detection", command=self.image_segmentation.edge_detection)
        edge_detection_btn.pack(pady=5, padx=10)

        # Button for Watershed Segmentation
        watershed_btn = CustomButton5(image_segmentation_frame, text="Apply Watershed", command=self.image_segmentation.watershed)
        watershed_btn.pack(pady=5, padx=10)

        # Button for GrabCut Segmentation
        grabcut_btn = CustomButton5(image_segmentation_frame, text="Apply GrabCut", command=self.image_segmentation.grabcut)
        grabcut_btn.pack(pady=5, padx=10)

        # Button for Region Growing Segmentation
        region_growing_btn = CustomButton5(image_segmentation_frame, text="Region Growing", command=self.image_segmentation.region_growing)
        region_growing_btn.pack(pady=(5,20), padx=10)
