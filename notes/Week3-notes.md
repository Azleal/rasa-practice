## week3 总结

1. 自定义action时需要引入rasa_sdk, 使用`pip install rasa_sdk`进行安装
2. 在 http://www.tianqiapi.com 上注册用户生成appId和secretKey进行接口调用.
3. `ActionQueryWeather`中通过tracker获得填充在slot中实体city, 然后作为查天气的接口参数进行天气查询. 并将得到的数据进行解析,返回格式化之后的天气查询语句.


### 运行截图
![image](/snapshots/query_weather.png)

### 注意:
  - 在`rasa train`之前要删除掉默认生成原有的model

### 参考:
  - https://rasa.com/docs/rasa/custom-actions
  - https://rasa.com/docs/action-server/sdk-actions
  - http://doc.tianqiapi.com/603579
  
