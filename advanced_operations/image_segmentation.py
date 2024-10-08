import cv2
import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage import minimum_filter, maximum_filter, median_filter
from utils.file_handler import FileHandler


class ImageSegmentation:
    def __init__(self, file_handler):
        self.file_handler = file_handler


    #----------add your functions here----------#    
    # Function to apply thresholding
    def thresholding(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            gray_image = cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2GRAY)
            _, thresholded_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
            self.file_handler.processed_img = cv2.cvtColor(thresholded_image, cv2.COLOR_GRAY2BGR)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Function to apply edge detection using Canny
    def edge_detection(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            gray_image = cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray_image, 100, 200)
            self.file_handler.processed_img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Function to apply Watershed segmentation
    def watershed(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            gray_image = cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

            # Noise removal using morphological operations
            kernel = np.ones((3, 3), np.uint8)
            opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
            sure_bg = cv2.dilate(opening, kernel, iterations=3)

            # Finding sure foreground area
            dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
            _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

            # Finding unknown region
            sure_fg = np.uint8(sure_fg)
            unknown = cv2.subtract(sure_bg, sure_fg)

            # Marker labelling
            _, markers = cv2.connectedComponents(sure_fg)
            markers = markers + 1
            markers[unknown == 255] = 0

            # Apply the Watershed algorithm
            self.file_handler.processed_img = cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2RGB)
            markers = cv2.watershed(self.file_handler.processed_img, markers)
            self.file_handler.processed_img[markers == -1] = [255, 0, 0]  # Mark boundaries in red

            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Function to apply GrabCut segmentation
    def grabcut(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            mask = np.zeros(self.file_handler.processed_img.shape[:2], np.uint8)
            bgd_model = np.zeros((1, 65), np.float64)
            fgd_model = np.zeros((1, 65), np.float64)
            
            rect = (50, 50, self.file_handler.processed_img.shape[1] - 100, self.file_handler.processed_img.shape[0] - 100)
            cv2.grabCut(self.file_handler.processed_img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
            self.file_handler.processed_img = self.file_handler.processed_img * mask2[:, :, np.newaxis]

            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)
 # Function to apply Region Growing segmentation
    # Function to apply Region Growing segmentation
    def region_growing(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()

            def region_grow(img, seed, threshold):
                h, w = img.shape
                segmented = np.zeros_like(img)
                seed_stack = [seed]
                while seed_stack:
                    x, y = seed_stack.pop()
                    if segmented[x, y] == 0 and img[x, y] < threshold:
                        segmented[x, y] = 255
                        if x > 0: seed_stack.append((x - 1, y))
                        if x < h - 1: seed_stack.append((x + 1, y))
                        if y > 0: seed_stack.append((x, y - 1))
                        if y < w - 1: seed_stack.append((x, y + 1))
                return segmented

            gray_image = cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2GRAY)
            seed_point = (int(gray_image.shape[0] / 2), int(gray_image.shape[1] / 2))  # Using center as seed point
            threshold = 100
            region_grown = region_grow(gray_image, seed_point, threshold)

            self.file_handler.processed_img = cv2.cvtColor(region_grown, cv2.COLOR_GRAY2BGR)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def undo_action(self):
        self.file_handler.undo_action()

    def redo_action(self):
        self.file_handler.redo_action()

        