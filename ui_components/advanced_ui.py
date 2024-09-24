import tkinter as tk
from tkinter import ttk
from .custom_buttons import CustomButton2, dGray

class AdvancedUI:
    def __init__(self, sidebar, filter, intensity_manipulation, image_segmentation):
        self.sidebar = sidebar
        self.filter = filter
        self.intensity_manipulation = intensity_manipulation
        self.image_segmentation = image_segmentation
        self.setup_advanced_ui()

    def setup_advanced_ui(self):
        tab2 = tk.Frame(self.sidebar, bg=dGray, bd=0)
        self.sidebar.add(tab2, text="Advanced")

        # Create a nested notebook inside tab2
        nested_notebook = ttk.Notebook(tab2)
        nested_notebook.pack(expand=1, fill='both')

        # Create tabs inside the nested notebook
        filters_tab = tk.Frame(nested_notebook, bg=dGray)
        intensity_tab = tk.Frame(nested_notebook, bg=dGray)
        segmentation_tab = tk.Frame(nested_notebook, bg=dGray)

        nested_notebook.add(filters_tab, text="Filters")
        nested_notebook.add(intensity_tab, text="Intensity Manipulation")
        nested_notebook.add(segmentation_tab, text="Image Segmentation")

        # -----Add buttons to the Filters tab------

        # Button to apply histogram equalization filter
        histogram_equalization_btn = CustomButton2(filters_tab, text="Apply Histogram Equalization", command=self.filter.filter_histogram_equalization)
        histogram_equalization_btn.pack(pady=10)

        # Button to apply CLAHE filter
        clahe_btn = CustomButton2(filters_tab, text="Apply CLAHE", command=self.filter.filter_clahe)
        clahe_btn.pack(pady=5)

        # Button to apply Minimum filter
        min_filter_btn = CustomButton2(filters_tab, text="Minimum Filter", command=self.filter.filter_minimum)
        min_filter_btn.pack(pady=10)

        # Button to apply Maximum filter
        max_filter_btn = CustomButton2(filters_tab, text="Maximum Filter", command=self.filter.filter_maximum)
        max_filter_btn.pack(pady=5)

        # Button to apply Median filter
        median_filter_btn = CustomButton2(filters_tab, text="Median Filter", command=self.filter.filter_median)
        median_filter_btn.pack(pady=5)

        # Button to apply Gaussian Blur filter
        gaussian_blur_btn = CustomButton2(filters_tab, text="Gaussian Blur", command=self.filter.filter_gaussian_blur)
        gaussian_blur_btn.pack(pady=5)

        # Button to apply Linear filter
        linear_filter_btn = CustomButton2(filters_tab, text="Apply Linear Filter", command=self.filter.filter_linear)
        linear_filter_btn.pack(pady=10)

        # -----Add buttons to the Intensity Manipulation tab------



        # -----Add buttons to the Image Segmentation tab------
