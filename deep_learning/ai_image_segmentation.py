import tensorflow as tf
import numpy as np
from PIL import Image
import segmentation_models as sm
import cv2

class AIImageSegmentation:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.model = self.load_model()
        print("AIImageSegmentation class initialized")

    def load_model(self):
        # Load a pre-trained model, e.g., Unet with ResNet34 backbone
        model = sm.Unet('resnet34', encoder_weights='imagenet')
        print("Model loaded successfully")
        return model

    def apply_segmentation(self):
        if self.file_handler.processed_img is not None:
            print("Processing image")
            # Preprocess the image
            img = self.file_handler.processed_img
            original_size = (img.shape[1], img.shape[0])  # (width, height)
            print(f"Original image size: {original_size}")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_resized = cv2.resize(img, (256, 256))
            img_resized = np.expand_dims(img_resized, axis=0)
            img_resized = img_resized / 255.0
            print(f"Resized image shape: {img_resized.shape}")

            # Predict the segmentation mask
            mask = self.model.predict(img_resized)[0]
            print(f"Predicted mask shape: {mask.shape}")
            mask = (mask > 0.5).astype(np.uint8) * 255
            print(f"Binary mask shape: {mask.shape}")

            # Resize mask to original image size
            mask_resized = cv2.resize(mask, original_size)
            mask_resized = np.stack((mask_resized,)*3, axis=-1)  # Convert to 3 channels
            print(f"Resized mask shape: {mask_resized.shape}")

            # Find contours in the mask
            contours, _ = cv2.findContours(mask_resized[:, :, 0], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            print(f"Number of contours found: {len(contours)}")

            # Draw bounding boxes
            labeled_img = img.copy()
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(labeled_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                print(f"Bounding box: x={x}, y={y}, w={w}, h={h}")

            # Display the labeled image
            self.file_handler.display_image(labeled_img, self.file_handler.img_canvas2)
            print("Image displayed with bounding boxes")
        else:
            print("No processed image found")