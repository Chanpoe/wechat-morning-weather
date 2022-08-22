# wechat-morning-weather
纯python编写的微信公众号每日发送天气功能

# 步骤：

1.需要有python基础  
2.注册微信公众号平台  https://mp.weixin.qq.com/debug/cgi-bin/sandboxinfo?action=showinfo&t=sandbox/index  进入测试（个人开发者无法发送模版消息，只能借助测试号）  
3.需要下面的内容（修改方法在下面会介绍）：  


![image](https://user-images.githubusercontent.com/84487466/185932772-ea4d8bde-02e1-44ea-8f44-be6f9802b7f1.png)
![image](https://user-images.githubusercontent.com/84487466/185932928-431770f1-d7d5-46b9-b0c6-dcb7a21697a0.png)
![image](https://user-images.githubusercontent.com/84487466/185933228-b2ca133a-a273-4004-9ffb-34d48904c0da.png)

测试模板内容：（自己修改内容，参数使用{{}}的方式，自己可以仿照WeChat.py中body字典里的data格式进行增减修改）

```
世界上最无敌可爱的宝早上好~
今天是{{date.DATA}}  {{week.DATA}} 
每天都是超级爱宝宝的一天~ 
当前{{province.DATA}}{{city.DATA}} 的天气是{{weather.DATA}}
平均温度{{temperature.DATA}}
空气湿度{{humidity.DATA}}
有{{winddirection.DATA}}风{{windpower.DATA}}级
今天也要好好欣赏自己的美哦~ 
今天是我们在一起的第{{togetherDays.DATA}}天
这{{togetherDays.DATA}}天里每一天都超级爱你哦~
距离宝的生日还有{{birthDays.DATA}}天
已经在给宝准备礼物啦~ 
Love You Forever~ 
{{hua.DATA}}
```



# 需要修改的地方：

最主要的修改位置是下面四个  


![修改1](https://user-images.githubusercontent.com/84487466/185930408-8c4f19b4-dc84-4bc1-89d9-1bd94cc6dd68.png)
![修改2](https://user-images.githubusercontent.com/84487466/185930650-a6314f5b-878f-44e9-bc51-77a2cee4724b.png)
![修改3](https://user-images.githubusercontent.com/84487466/185930905-f1f0391f-3a22-433e-b6f1-fd0229600d07.png)
![image](https://user-images.githubusercontent.com/84487466/185931654-bc224b0a-d42a-4062-ad6f-4505f6ae11bc.png)

其他的地方按需修改（注释和英文单词应该好理解）  

# Ps：
  如果需要修改文字颜色可以参照  https://www.chanpoe.top/rgb  复制RGB对应的十六进制码替换color的值即可
 
