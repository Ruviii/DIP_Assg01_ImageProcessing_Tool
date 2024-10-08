class AIImageSegmentation:
    def __init__(self, file_handler):
        self.file_handler = file_handler



    def undo_action(self):
        self.file_handler.undo_action()

    def redo_action(self):
        self.file_handler.redo_action()