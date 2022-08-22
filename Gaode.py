import requests

# 高德天气查询平台 https://lbs.amap.com/api/webservice/guide/api/weatherinfo
# 选择Web服务获取key 教程：https://blog.csdn.net/gz2580/article/details/111088190

key = 'xxxxxxxxxxxxxxxxxxxxxxx'
# adcode 城市编码表下载：https://lbs.amap.com/api/webservice/download
# 江夏区 420115
# 大同城区 140213
city_code = 'xxxxxx'

weather_url = f'https://restapi.amap.com/v3/weather/weatherInfo?key={key}&city={city_code}'

def getWeather():
    weather_response = requests.get(weather_url)
    return weather_response.json()
