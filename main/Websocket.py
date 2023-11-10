import datetime
import json
from websocket import create_connection

from src.tools import CustomizedTools
import Processor


class Websocket:
    def __init__(self, name):
        self.sorted_message1 = None
        self.sorted_message2 = None
        self.received_message1 = None
        self.received_message2 = None
        self.first_answer = None
        self.ws = None
        self.message_Id1 = -1
        self.message_Id2 = -1
        self.name = name

    def websocketConnection(self):
        ws = create_connection("ws://chat.idnsportal.com:444")  # 建立连接
        ws_status = ws.getstatus()  # 获取连接状态
        self.ws = ws

        print("获取连接状态:", ws_status)
        return ws_status

    def sendFirstRequest(self, first_request):
        self.ws.send(first_request)  # 发送请求参数
        self.first_answer = self.ws.recv()
        print("返回:", self.first_answer)

    def getMessage(self):
        self.received_message1 = self.ws.recv()  # 获取返回的消息记录
        cut_message = self.cutMessage(1)
        # print(self.received_message)
        if cut_message is None:
            self.getMessage()
            return
        else:
            print(cut_message[1])
            return cut_message[0]

    def cutMessage(self, n):
        if n == 1:
            received_message = json.loads(self.received_message1)
        elif n == 2 and "data" not in self.received_message2:
            # print(self.received_message2)
            received_message = json.loads(self.received_message2)
        else:
            return
        # print(received_message)
        if "message" in received_message:
            time_stamp13 = received_message["message"]['created']
            label = received_message["message"]['label']
            message_id = received_message["message"]['messageId']
            name = received_message["message"]['name']
            message_text = received_message["message"]['text']  # 拆json，将值存储到变量
            time = CustomizedTools.TimeStampToTime(time_stamp13)  # 时间戳转时间

            cut_message = f"[{time}]{name}({label}): {message_text} ({message_id})"
            sorted_message = {"original": received_message, "time_stamp13": time_stamp13, "label": label,
                              "message_id": message_id, "name": name, "message_text": message_text
                              }
            if n == 1:
                self.sorted_message1 = sorted_message
            if n == 2:
                self.sorted_message2 = sorted_message
            return sorted_message, cut_message

        else:
            return

    def processMessage(self):
        if self.sorted_message2 is not None:
            sorted_message = self.sorted_message2
            processor = Processor.Processor()
            result = processor.searchCommand(sorted_message, self.name)
            return result

    def noticeMessage(self):
        self.received_message2 = self.ws.recv()  # 获取返回的消息记录
        cut_message = self.cutMessage(2)
        # print(self.received_message)
        if cut_message is None:
            self.noticeMessage()
            return
        else:
            return cut_message[0]

    def sendMessage(self, text):
        request = '{"type" : "message","group" : "idns_cn","name" : ' + self.name + ',"text" : "' + text + '","date" : ' + str(
            CustomizedTools.getTimeStamp()) + '}'
        # print(request)
        self.ws.send(request)
        print(f"{'['+str(datetime.datetime.now())+']'}已发送: \n{text}\n")
