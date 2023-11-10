from src.plugins.Echo import *
from src.plugins.ChooseSongs import *
from src.plugins.Weather import *
from src.plugins.Ping import *
import datetime


class Processor:
    def __init__(self):
        self.text_after_command = None
        self.message = None
        self.command = None
        self.name = None

    def searchCommand(self, message: dict, name):
        self.message = message
        self.name = name

        text = message["message_text"]
        #  print(text)
        if text[0] == "~":
            print(f"[{datetime.datetime.now()}]:received keywords")
            command = re.search(r"(?<=^~).+?(?=\s)", text)
            if command is not None:
                #  print(command.group())
                self.command = command.group()
                return self.processMessage()

    def processMessage(self):
        self.text_after_command = re.search(r"(?<=\s).+", self.message["message_text"]).group()
        if self.command == "echo":
            result = Echo().main(self.text_after_command, self.name)
        elif self.command == "点歌":
            result = ChooseSongs().main(self.text_after_command)
        elif self.command == "ping":
            result = Ping().main(self.text_after_command)

        # elif self.command == "天气":
        #     result = Weather().main(self.message)

        else:
            return
        return result
