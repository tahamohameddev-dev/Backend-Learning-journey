

class phone:
    def __init__(self, type, color, is_android):
        self.type = type
        self.color = color
        self.is_android = is_android

    def is_infinix(self):
        if self.type == "infinix":
            return True
        else:
            return False