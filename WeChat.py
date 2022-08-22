import requests
import json
import datetime
import re

# APP的ID号
appID = 'xxxxxxxxxxx'
# 安全秘钥
appsecret = 'xxxxxxxxxxxxxxxxxxxxxx'


# 获取access_token
def getAccessToken():
    r1 = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            "appid": appID,
            "secret": appsecret
        }
    )
    access_token = r1.json()['access_token']
    # print(access_token)
    return access_token


# 发送天气提醒推送
def sendMessage(weatherData, wx_id, template_id):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    # 在一起的日期
    togetherDay = datetime.date(1999, 1, 1)
    # 她的下一个生日
    herBirthday = datetime.date(1999, 1, 1)

    today = datetime.date(int(year), int(month), int(day))
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    body = {
        "touser": wx_id,  # 推送消息的对象（用户微信id）
        "template_id": template_id,  # 模板ID
        "data": {
            'date': {
                'value': datetime.datetime.now().strftime('%Y-%m-%d'),
                'color': '#228B22'
            },
            'week': {
                'value': week_list[datetime.date(year, month, day).weekday()],
                'color': '#228B22'
            },
            'province': {
                'value': weatherData['lives'][0]['province'],
                'color': '#FF6347'
            },
            'city': {
                'value': weatherData['lives'][0]['city'],
                'color': '#FF6347'
            },
            'weather': {
                'value': weatherData['lives'][0]['weather'],
                'color': '#FF8C00'
            },
            'temperature': {
                'value': weatherData['lives'][0]['temperature'] + '℃',
                'color': '#8A2BE2'
            },
            'humidity': {
                'value': weatherData['lives'][0]['humidity'] + '%',
                'color': '#FF69B4'
            },
            'winddirection': {
                'value': weatherData['lives'][0]['winddirection'],
                'color': '#00BFFF'
            },
            'windpower': {
                'value': weatherData['lives'][0]['windpower'],
                'color': '#00BFFF'
            },
            'togetherDays': {
                'value': int(re.search('(?P<days>.*?) days', str(today.__sub__(togetherDay))).group('days')) + 1,
                'color': '#FF4500'
            },
            'birthDays': {
                'value': int(re.search('(?P<days>.*?) days', str(herBirthday.__sub__(today))).group('days')),
                'color': '#FFD700'
            },
            'hua': {  # 情话
                'value': '',
                'color': '#FF0000'
            }
        }
    }

    r2 = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/template/send",
        params={
            "access_token": getAccessToken()
        },
        data=json.dumps(body)
    )

    print(r2.text)



