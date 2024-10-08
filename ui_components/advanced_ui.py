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
        s_frame = ctk.CTkScrollableFrame(tab2, width=200, height=400, fg_color=color_2)
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

        # Button to apply Sharpening filter
        sharpen_btn = CustomButton4(filters_frame, text="Sharpen", command=self.filter.sharpen_image)
        sharpen_btn.pack(pady=(25,10), padx=10)

        # Button to apply Smoothing filter
        smooth_btn = CustomButton4(filters_frame, text="Smooth", command=self.filter.smooth_image)
        smooth_btn.pack(pady=10, padx=10)

        # Button to apply Edge Detection filter
        edge_detection_btn = CustomButton4(filters_frame, text="Edge Detection", command=self.filter.edge_detection)
        edge_detection_btn.pack(pady=10, padx=10)

        # Button to apply Embossing filter
        embossing_btn = CustomButton4(filters_frame, text="Emboss", command=self.filter.emboss_image)
        embossing_btn.pack(pady=10, padx=10)

        # Button to apply Gaussian Blur filter
        gaussian_blur_btn = CustomButton4(filters_frame, text="Gaussian Blur", command=self.filter.gaussian_blur)
        gaussian_blur_btn.pack(pady=10, padx=10)

        # Button to apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
        bilateral_filter_btn = CustomButton4(filters_frame, text="Bilateral", command=self.filter.bilateral_filter)
        bilateral_filter_btn.pack(pady=(10,25), padx=10)

        # -----Add buttons to the Intensity Manipulation tab------

        # Button to apply negative transformation
        negative_transformation_btn = CustomButton3(intensity_manipulation_frame, text="Negative", command=self.intensity_manipulation.negative_transformation)
        negative_transformation_btn.pack(pady=(25,10), padx=10)

        # Button to apply logarithmic transformation
        log_transformation_btn = CustomButton3(intensity_manipulation_frame, text="Brighten", command=self.intensity_manipulation.log_transformation)
        log_transformation_btn.pack(pady=10, padx=10)

        # Button to apply power-law (gamma) transformation
        power_law_transformation_btn = CustomButton3(intensity_manipulation_frame, text="Adjust Gamma", command=self.intensity_manipulation.power_law_transformation)
        power_law_transformation_btn.pack(pady=10, padx=10)

        # Button to apply contrast stretching
        contrast_stretching_btn = CustomButton3(intensity_manipulation_frame, text="Enhance Contrast", command=self.intensity_manipulation.contrast_stretching)
        contrast_stretching_btn.pack(pady=10, padx=10)

        # Button to apply intensity level slicing
        intensity_level_slicing_btn = CustomButton3(intensity_manipulation_frame, text="Slice Levels", command=self.intensity_manipulation.intensity_level_slicing)
        intensity_level_slicing_btn.pack(pady=10, padx=10)

        # Button to apply global histogram equalization
        apply_histogram_equalization_btn = CustomButton3(intensity_manipulation_frame, text="Equalize Histogram", command=self.intensity_manipulation.apply_histogram_equalization)
        apply_histogram_equalization_btn.pack(pady=10, padx=10)

        # Button to apply local histogram equalization (CLAHE)
        apply_local_histogram_equalization_btn = CustomButton3(intensity_manipulation_frame, text="Local Equalization", command=self.intensity_manipulation.apply_local_histogram_equalization)
        apply_local_histogram_equalization_btn.pack(pady=10, padx=10)

        # Button to apply tonal transformation
        tonal_transformation_btn = CustomButton3(intensity_manipulation_frame, text="Adjust Tones", command=self.intensity_manipulation.tonal_transformation)
        tonal_transformation_btn.pack(pady=10, padx=10)

        # Button to apply color balancing
        color_balancing_btn = CustomButton3(intensity_manipulation_frame, text="Balance Colors", command=self.intensity_manipulation.color_balancing)
        color_balancing_btn.pack(pady=(10,25), padx=10)


        # -----Add buttons to the Image Segmentation tab------

        # Button for Thresholding Segmentation
        thresholding_btn = CustomButton5(image_segmentation_frame, text="Apply Thresholding", command=self.image_segmentation.thresholding)
        thresholding_btn.pack(pady=(25,10), padx=10)

        # Button for Edge Detection
        edge_detection_btn = CustomButton5(image_segmentation_frame, text="Edge Detection", command=self.image_segmentation.edge_detection)
        edge_detection_btn.pack(pady=10, padx=10)

        # Button for Watershed Segmentation
        watershed_btn = CustomButton5(image_segmentation_frame, text="Apply Watershed", command=self.image_segmentation.watershed)
        watershed_btn.pack(pady=10, padx=10)

        # Button for GrabCut Segmentation
        grabcut_btn = CustomButton5(image_segmentation_frame, text="Apply GrabCut", command=self.image_segmentation.grabcut)
        grabcut_btn.pack(pady=10, padx=10)

        # Button for Region Growing Segmentation
        region_growing_btn = CustomButton5(image_segmentation_frame, text="Region Growing", command=self.image_segmentation.region_growing)
        region_growing_btn.pack(pady=(10,25), padx=10)


        
        

