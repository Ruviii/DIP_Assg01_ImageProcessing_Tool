import cv2
import numpy as np
from PIL import Image, ImageEnhance

class IntensityManipulation:
    def __init__(self, file_handler):
        self.file_handler = file_handler

     # Negative Transformation: Reverse the pixel intensity
    def negative_transformation(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            self.file_handler.processed_img = cv2.bitwise_not(self.file_handler.processed_img)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Logarithmic Transformation
    def log_transformation(self, c=1):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            image = np.float32(self.file_handler.processed_img)
            image_log = c * np.log1p(image)
            self.file_handler.processed_img = cv2.normalize(image_log, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Power-Law (Gamma) Transformation
    def power_law_transformation(self, gamma=1.0, c=1):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            image = np.float32(self.file_handler.processed_img) / 255.0
            image_gamma = c * np.power(image, gamma)
            self.file_handler.processed_img = cv2.normalize(image_gamma, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Contrast Stretching: Expands the dynamic range of intensities
    def contrast_stretching(self, r1, r2, s1, s2):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            image = np.float32(self.file_handler.processed_img)
            output_image = np.piecewise(image,
                [image <= r1, (image > r1) & (image <= r2), image > r2],
                [lambda i: (s1 / r1) * i,
                 lambda i: ((s2 - s1) / (r2 - r1)) * (i - r1) + s1,
                 lambda i: ((255 - s2) / (255 - r2)) * (i - r2) + s2]
            )
            self.file_handler.processed_img = output_image.astype(np.uint8)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Intensity Level Slicing
    def intensity_level_slicing(self, lower_bound, upper_bound, background_value=0):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            image = np.float32(self.file_handler.processed_img)
            sliced_image = np.where((image >= lower_bound) & (image <= upper_bound), 255, background_value)
            self.file_handler.processed_img = sliced_image.astype(np.uint8)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Histogram Equalization: Global
    def apply_histogram_equalization(self):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            if len(self.file_handler.processed_img.shape) == 2:  # Grayscale image
                self.file_handler.processed_img = cv2.equalizeHist(self.file_handler.processed_img)
            elif len(self.file_handler.processed_img.shape) == 3:  # Color image
                yuv_img = cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2YUV)
                yuv_img[:, :, 0] = cv2.equalizeHist(yuv_img[:, :, 0])
                self.file_handler.processed_img = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2BGR)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Local Histogram Equalization using CLAHE
    def apply_local_histogram_equalization(self, clip_limit=2.0, tile_grid_size=(8, 8)):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
            if len(self.file_handler.processed_img.shape) == 2:  # Grayscale image
                self.file_handler.processed_img = clahe.apply(self.file_handler.processed_img)
            elif len(self.file_handler.processed_img.shape) == 3:  # Color image
                lab_img = cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2LAB)
                lab_img[:, :, 0] = clahe.apply(lab_img[:, :, 0])
                self.file_handler.processed_img = cv2.cvtColor(lab_img, cv2.COLOR_LAB2BGR)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Tonal Transformation: Adjusts the contrast of the image
    def tonal_transformation(self, factor=1.5):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            img_pil = Image.fromarray(cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2RGB))
            enhancer = ImageEnhance.Contrast(img_pil)
            img_pil = enhancer.enhance(factor)  # Enhance contrast by the given factor (1.0 = original)
            self.file_handler.processed_img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    # Color Balancing: Adjust the balance of red, green, and blue channels
    def color_balancing(self, red_balance=1.0, green_balance=1.0, blue_balance=1.0):
        if self.file_handler.processed_img is not None:
            self.file_handler.save_undo_state()
            img_pil = Image.fromarray(cv2.cvtColor(self.file_handler.processed_img, cv2.COLOR_BGR2RGB))
            r, g, b = img_pil.split()

            # Apply balance to each channel
            r = r.point(lambda i: i * red_balance)
            g = g.point(lambda i: i * green_balance)
            b = b.point(lambda i: i * blue_balance)

            # Merge the channels back
            img_pil = Image.merge('RGB', (r, g, b))
            self.file_handler.processed_img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
            self.file_handler.display_image(self.file_handler.processed_img, self.file_handler.img_canvas2)

    def undo_action(self):
        self.file_handler.undo_action()

    def redo_action(self):
        self.file_handler.redo_action()