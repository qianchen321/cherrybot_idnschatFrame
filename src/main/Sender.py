from Websocket import create_connection
import datetime
import time

name = f'"{input("你的名字:")}"'


def getTime():
    s = int(time.time() // 100)
    ms = int(datetime.datetime.now().microsecond)
    t = str(s) + str(ms)
    return t


class Main:
    def __init__(self):
        self.ws = None
        self.message_Id = -1

    def websocketConnection(self):
        # 建立连接
        ws = create_connection("ws://chat.idnsportal.com:444")

        # 获取连接状态
        print("获取连接状态: ", ws.getstatus())
        self.ws = ws

    def firstRequest(self, text):
        # 发送请求参数
        self.ws.send(text)
        # 获取返回结果
        result = self.ws.recv()
        print(result)

    def send(self, text):
        self.ws.send(
            '{"type" : "message","group" : "idns_cn","name" : ' + name + ',"text" : "' + text + '","date" : ' + str(
                getTime()) + '}')


connection = Main()


def main():
    try:
        connection.websocketConnection()
        connection.firstRequest(
            '{"name":' + name + ',"type":"init","group":"idns_cn","country":"CN","lastMessageId":"' + str(
                connection.message_Id) + '", "date":"' + str(
                getTime()) + '","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"}')
        while True:
            inp = input("你要说什么：\n")
            connection.send(inp)
    except TypeError and ConnectionError:
        connection.ws.close()
        main()

if __name__ == "__main__":
    main()
