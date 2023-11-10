from src.tools import CustomizedTools
import re


class Echo:
    def __init__(self):
        self.message = None
        self.name = None

    def main(self, message: str, name):
        self.message = message
        self.name = name

        # send_message = '{"type" : "message","group" : "idns_cn","name" : ' + self.name + ',"text" : ' + self.message + ',"date" : ' + str(CustomizedTools.getTimeStamp()) + '}'
        return self.message

