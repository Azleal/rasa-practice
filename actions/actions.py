# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

import requests

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionQueryWeather(Action):
   def name(self) -> Text:
      return "action_query_weather"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot('city')
        res = requests.get("http://www.tianqiapi.com/free/day?version=v9&appid=68438168&appsecret=V38NXdnn&city=" + city)
        if res.ok:
            weather_detail = res.json()
        else:
            dispatcher.utter_message(text='获取天气信息异常')
            return []
        response = "{}今日天气{}， 当前气温{}摄氏度，白天气温{}摄氏度，夜间气温{}摄氏度，风力为{}的{}，空气指数{}".format(weather_detail['city'], weather_detail['wea'], weather_detail['tem'], weather_detail['tem_day'], weather_detail['tem_night'],  weather_detail['win_meter'], weather_detail['win'], weather_detail['air'])
        dispatcher.utter_message(text=response)

        return [AllSlotsReset()]
