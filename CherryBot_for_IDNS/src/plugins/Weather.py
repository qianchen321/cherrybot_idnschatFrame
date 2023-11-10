import json
import requests
import re


r'''class Weather:
    def __init__(self):
        self.message = None
        self.name = None

    def main(self, message):
        self.message = message

        city = re.search(r"(?<=\s).+", self.message["message_text"]).group()
        if city in ['列宁格勒', '斯大林格勒']:  # 如果参数不符合要求，则提示用户重新输入
            # 可以使用平台的 Message 类直接构造模板消息
            return "你想查询的城市暂不支持，请重新输入！"
        else:
            city_weather = self.get_weather(city)
            return city_weather

    # 在这里编写获取天气信息的函数
    def get_weather(self, city: str) -> str:
        url = f'https://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city={city}&latitude=39.902895&longitude=116.427915&needMoreData=true&pageNo=1&pageSize=7'
        api_request = requests.get(url)
        api_get = json.loads(api_request.text)
        if api_get["msg"] != "查询天气服务返回结果为空":
            # await weather.send(message=str(api_get))
            print(api_get["msg"])
            weather_list = api_get["data"]["list"][0]
            date = weather_list["date"]
            weather_like = weather_list["weather"]
            temperature = weather_list["temp"]
            humidity = weather_list["humidity"]
            wind = weather_list["wind"]
            high_temp = weather_list["high"]
            low_temp = weather_list["low"]
            air_data = weather_list["airData"]
            air_quality = weather_list["airQuality"]
            weather_send = f"{city} {date}\n{low_temp}℃~{high_temp}℃\n空气质量:{air_quality},污染指数:{air_data}\n当前天气:{weather_like},温度:{temperature}℃,湿度:{humidity},风向:{wind}"
        else:
            weather_send = f"你想查询的城市 {city} 暂不支持"
        return weather_send
'''