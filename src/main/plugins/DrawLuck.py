import random
from datetime import date
import json
import os


def luck_simple(num):
    if num > 98:
        return ",,ԾㅂԾ,,绝对没错，你就是传说中的天选之人！"
    elif num > 94:
        return "大吉！今日的幸运儿就是你！"
    elif num > 85:
        return "吉，真不错呢！"
    elif num > 75:
        return "半吉，嗯，很不错"
    elif num > 59:
        return "小吉，嗯，还行"
    elif num > 29:
        return "末小吉，嗯……"
    elif num > 9:
        return "凶，大事不妙……"
    else:
        return "大凶!?!"


class DrawLuck:
    def __init__(self):
        self.message = None
        self.username = None

    def main(self, username):
        self.username = username

        userid = self.userid()
        rnd = random.Random()
        rnd.seed(int(date.today().strftime("%y%m%d")) + int(userid))
        lucknum = rnd.randint(1, 100)
        return f"{username}你今日的幸运指数是{lucknum}/100，{luck_simple(lucknum)}"

    def userid(self) -> int:
        if os.path.exists(os.path.dirname(__file__)+r"\temp\DrawLuck.json"):
            pass
        else:
            f = open(os.path.dirname(__file__)+r"\temp\DrawLuck.json", 'w')
            f.write("{}")
            f.close()

        with open(os.path.dirname(__file__)+r"\temp\DrawLuck.json", encoding='utf-8') as file:
            data = json.load(file)
            file.close()
        if self.username not in data:
            data[self.username] = len(data) + 1
            with open(os.path.dirname(__file__) + r"\temp\DrawLuck.json", 'w',  encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False)
                file.close()
        else:
            pass
        return data[self.username]
