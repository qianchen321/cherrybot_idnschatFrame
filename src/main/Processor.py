from plugins.Echo import *
from plugins.ChooseSongs import *
from plugins.Weather import *
from plugins.Ping import *
from plugins.DrawLuck import *
from plugins.Menu import *
import datetime
import tools.ConsoleTools as ConsoleTools


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
            print(f"{ConsoleTools.console_colour('INFO')}[{datetime.datetime.now()}]:received keywords")
            command = re.search(r"(?<=^~).+?(?=\s)", text)
            if command is None:
                #  print(command.group())
                command = re.search(r"(?<=^~).+", text)
            self.command = command.group()
            return self.processMessage()

    def processMessage(self):
        text_after_command = re.search(r"(?<=\s).+", self.message["message_text"])
        if text_after_command is not None:
            self.text_after_command = text_after_command.group()

        if self.command == "echo":
            result = Echo().main(self.text_after_command, self.name)
        elif self.command == "点歌":
            result = ChooseSongs().main(self.text_after_command)
        elif self.command == "ping":
            result = Ping().main(self.text_after_command)
        elif self.command == "draw":
            result = DrawLuck().main(self.message["name"])
        elif self.command == ("menu" or "菜单"):
            result = Menu().main(self.text_after_command, self.name)

        # elif self.command == "天气":
        #     result = Weather().main(self.message)

        else:
            return
        return result
