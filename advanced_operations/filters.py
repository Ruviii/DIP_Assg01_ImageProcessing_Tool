import cv2
import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage import minimum_filter, maximum_filter, median_filter
from utils.file_handler import FileHandler

class Filters:
    def __init__(self, file_handler):
        self.file_handler = file_handler

    # Function to apply histogram equalization
    def apply_histogram_equalization(self, image):
        if image is not None:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            equalized_image = cv2.equalizeHist(gray_image)
            equalized_image_bgr = cv2.cvtColor(equalized_image, cv2.COLOR_GRAY2BGR)
            return equalized_image_bgr
        return None

    # Function to apply CLAHE
    def apply_clahe(self, image):
        if image is not None:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            clahe_image = clahe.apply(gray_image)
            clahe_image_bgr = cv2.cvtColor(clahe_image, cv2.COLOR_GRAY2BGR)
            return clahe_image_bgr
        return None

    # Function to apply histogram equalization filter
    def filter_histogram_equalization(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            self.file_handler.processed_img = self.apply_histogram_equalization(self.file_handler.processed_img)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Function to apply CLAHE filter
    def filter_clahe(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            self.file_handler.processed_img = self.apply_clahe(self.file_handler.processed_img)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Function to apply minimum filter
    def apply_minimum_filter(self, image):
        if image is not None:
            filtered_image = minimum_filter(image, size=3)
            return filtered_image
        return None

    # Function to apply maximum filter
    def apply_maximum_filter(self, image):
        if image is not None:
            filtered_image = maximum_filter(image, size=3)
            return filtered_image
        return None

    # Function to apply median filter
    def apply_median_filter(self, image):
        if image is not None:
            filtered_image = median_filter(image, size=3)
            return filtered_image
        return None

    # Function to apply Gaussian blur
    def apply_gaussian_blur(self, image):
        if image is not None:
            gaussian_filter = np.array([
                [1/13, 1/8, 1/13],
                [1/8, 1/5, 1/8],
                [1/13, 1/8, 1/13]
            ])
            filtered_image = cv2.filter2D(image, -1, gaussian_filter)
            return filtered_image
        return None

    # Functions to apply each filter and update the displayed image
    def filter_minimum(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            self.file_handler.processed_img = self.apply_minimum_filter(self.file_handler.processed_img)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def filter_maximum(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            self.file_handler.processed_img = self.apply_maximum_filter(self.file_handler.processed_img)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def filter_median(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            self.file_handler.processed_img = self.apply_median_filter(self.file_handler.processed_img)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def filter_gaussian_blur(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            self.file_handler.processed_img = self.apply_gaussian_blur(self.file_handler.processed_img)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def apply_linear_filter(self, image):
        if image is not None:
            # Convert to grayscale if the image is in color
            if len(image.shape) == 3:  # Check if the image is colored
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Define the mean filter (3x3)
            mean_filter = np.ones((3, 3), dtype=np.float32) / 9
            
            # Apply filter using cv2.filter2D
            filtered_image = cv2.filter2D(image, -1, mean_filter)
            
            # Apply filter using convolve2d
            filtered_image_2 = convolve2d(image, mean_filter, mode='same')
            filtered_normalized = np.clip(filtered_image_2, 0, 255)
            filtered_normalized = filtered_normalized.astype(np.uint8)
            
            return filtered_image, filtered_normalized
        return None, None

    def filter_linear(self):
        if self.file_handler.processed_img is not None:
            filtered_image, filtered_normalized = self.apply_linear_filter(self.file_handler.processed_img)
            if filtered_image is not None:
                self.file_handler.display_image(filtered_normalized, self.file_handler.img_canvas2)

    def undo_action(self):
        self.file_handler.undo_action()

    def redo_action(self):
        self.file_handler.redo_action()