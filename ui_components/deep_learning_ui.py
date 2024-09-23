import tkinter as tk
from .custom_buttons import CustomButton2, dGray

class DeepLearningUI:
    def __init__(self, sidebar, style_transfer, image_enhancement, image_generator, ai_image_segmentation):
        self.sidebar = sidebar
        self.style_transfer = style_transfer
        self.image_enhancement = image_enhancement
        self.image_generator = image_generator
        self.ai_image_segmentation = ai_image_segmentation
        self.setup_deep_learning_ui()

    def setup_deep_learning_ui(self):
        tab3 = tk.Frame(self.sidebar, bg=dGray, bd=0)
        self.sidebar.add(tab3, text="AI Tools")

        # Undo button
        undo_btn = CustomButton2(tab3, text="Undo", command=self.undo_action)
        undo_btn.pack(pady=10)

        # Redo button
        redo_btn = CustomButton2(tab3, text="Redo", command=self.redo_action)
        redo_btn.pack(pady=10)

    def undo_action(self):
        self.style_transfer.undo_action()
        self.image_enhancement.undo_action()
        self.image_generator.undo_action()
        self.ai_image_segmentation.undo_action()

    def redo_action(self):
        self.style_transfer.redo_action()
        self.image_enhancement.redo_action()
        self.image_generator.redo_action()
        self.ai_image_segmentation.redo_action()

    #----------buttons for ai_image_segmentation----------#

    #----------buttons for image_enhancement----------#

    #----------buttons for image_generator----------#

    #----------buttons for style_transfer----------#