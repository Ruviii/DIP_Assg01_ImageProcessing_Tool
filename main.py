import tkinter as tk
from utils.file_handler import FileHandler
from basic_operations.basic_processor import BasicProcessor
from advanced_operations.filters import Filters
from advanced_operations.image_segmentation import ImageSegmentation
from advanced_operations.intensity_manipulation import IntensityManipulation
from deep_learning.style_transfer import StyleTransfer
from deep_learning.ai_image_segmentation import AIImageSegmentation
from ui_components.main_ui import MainUI
from ui_components.basic_ui import BasicUI
from ui_components.advanced_ui import AdvancedUI
from ui_components.deep_learning_ui import DeepLearningUI

if __name__ == "__main__":
    root = tk.Tk()
    file_handler = FileHandler()
    basic_processor = BasicProcessor(file_handler)
    filters = Filters(file_handler)
    image_segmentation = ImageSegmentation(file_handler)
    intensity_manipulation = IntensityManipulation(file_handler)
    ai_image_segmentation = AIImageSegmentation(file_handler)
    style_transfer = StyleTransfer(file_handler)

    main_ui = MainUI(root, file_handler)
    basic_ui = BasicUI(main_ui.sidebar, basic_processor)
    advanced_ui = AdvancedUI(main_ui.sidebar, filters, intensity_manipulation, image_segmentation)
    deep_learning_ui = DeepLearningUI(main_ui.sidebar, style_transfer, ai_image_segmentation)
    root.mainloop()