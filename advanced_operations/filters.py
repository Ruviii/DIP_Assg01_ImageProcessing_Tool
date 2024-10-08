import cv2
import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage import minimum_filter, maximum_filter, median_filter
from utils.file_handler import FileHandler

class Filters:
    def __init__(self, file_handler):
        self.file_handler = file_handler

    def sharpen_image(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])  # Sharpening kernel
            sharpened_img = cv2.filter2D(self.file_handler.processed_img, -1, kernel)
            self.file_handler.processed_img = sharpened_img
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def smooth_image(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            smoothed_img = cv2.GaussianBlur(self.file_handler.processed_img, (5, 5), 0)
            self.file_handler.processed_img = smoothed_img
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def edge_detection(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            edges = cv2.Canny(self.file_handler.processed_img, 100, 200)
            self.file_handler.processed_img = edges
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def emboss_image(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            kernel = np.array([[0, -1, -1], [1, 0, -1], [1, 1, 0]])  # Emboss kernel
            embossed_img = cv2.filter2D(self.file_handler.processed_img, -1, kernel)
            self.file_handler.processed_img = embossed_img
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def gaussian_blur(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            blurred_img = cv2.GaussianBlur(self.file_handler.processed_img, (15, 15), 0)
            self.file_handler.processed_img = blurred_img
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def bilateral_filter(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            # Applying Bilateral Filter
            bilateral_img = cv2.bilateralFilter(self.file_handler.processed_img, d=9, sigmaColor=75, sigmaSpace=75)
            self.file_handler.processed_img = bilateral_img
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)




    def undo_action(self):
        self.file_handler.undo_action()

    def redo_action(self):
        self.file_handler.redo_action()