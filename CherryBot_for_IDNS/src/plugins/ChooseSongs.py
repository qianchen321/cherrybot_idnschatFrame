import requests


class ChooseSongs:
    def __init__(self):
        self.message = None

    def main(self, message: str):
        self.message = message
        answer = requests.get(f"http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={self.message}&type=1&offset=0&total=true&limit=2").json()
        try:
            # print(answer["result"]["songs"][0]["id"])
            return f"http://music.163.com/song/media/outer/url?id={answer['result']['songs'][0]['id']}.mp3\n这是你点的歌，请慢用~"
        except KeyError:
            return "没有你想要的歌曲"
