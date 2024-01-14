from ping3 import ping


class Ping:
    def __init__(self):
        self.message = None

    def main(self, message: str):
        self.message = message
        # print(self.message)
        if self.message != "":
            delay = ping_host(self.message)
            if delay:
                return f"已为网站测速\n{self.message}延迟{delay}ms"
            else:
                return f"测速失败！\n也许是无法连接网站或延迟过高，也可能是输入的网址不正确！"
        # else:
        #     dir_path = os.path.dirname(__file__)
        #     f = open(dir_path + r"\cmd.txt", encoding='utf-8')
        #     text = f.read()
        #     f.close()
        #     return text)
        else:
            return f"测速失败！\n无法连接网站或输入的网址不正确！"


def ping_host(ip):
    ip_address = ip
    response = ping(ip_address)
    # print(response)
    if response is not None:
        delay = int(response * 1000)
        return delay
    else:
        return False
