import Gaode
import WeChat

# 微信id列表 给谁发加谁
wx_id = ["o7sy75wV5eQHQCa8xobmG0f31-0A", "o7sy75y-HE1dWs0ll0Oklv2oH254"]
# 模板消息id
template_id = 'XjOfYJgsxGYh7CpcD0qEe53PTqQocTQNRcUcuTEoOMk'

# 获取天气数据
weatherData = Gaode.getWeather()

if __name__ == '__main__':
    for a_id in wx_id:
        WeChat.sendMessage(weatherData, a_id, template_id)
