import tkinter as tk
from .custom_buttons import CustomButton3,CustomButton4,CustomButton5, color_2

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

    #----------buttons for ai_image_segmentation----------#

    #----------buttons for image_enhancement----------#

    #----------buttons for image_generator----------#

    #----------buttons for style_transfer----------#