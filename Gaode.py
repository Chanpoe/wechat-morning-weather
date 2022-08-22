import requests

# 高德天气查询平台 https://lbs.amap.com/api/webservice/guide/api/weatherinfo

key = '633d4682a142fc65959f68248abc12b7'
# adcode 城市编码表下载：https://lbs.amap.com/api/webservice/download
# 江夏区 420115
# 大同城区 140213
city_code = '140213'

weather_url = f'https://restapi.amap.com/v3/weather/weatherInfo?key={key}&city={city_code}'

# weather_response = requests.get(weather_url)
# {"status": "1", "count": "1", "info": "OK", "infocode": "10000", "lives": [
#     {"province": "山西", "city": "平城区", "adcode": "140213", "weather": "晴", "temperature": "24", "winddirection": "北",
#      "windpower": "5", "humidity": "36", "reporttime": "2022-08-22 16:10:05"}]}

# print(weather_response.text)

def getWeather():
    weather_response = requests.get(weather_url)
    return weather_response.json()
