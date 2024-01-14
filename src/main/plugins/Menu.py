import os


class Menu:
    def __init__(self):
        self.message = None
        self.name = None

    def main(self, message: str, name):
        file = open(os.path.dirname(__file__) + r"\Menu.txt", 'r', encoding='utf-8')
        text = ""
        contents = file.readlines()
        for i in contents:
            text += i
        file.close()
        # print(rf"{file.read()}")
        # print(text)
        return str(text)

