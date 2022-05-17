# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests


def Weather(city):
    api_key = "3c0b20a112faaef8c985d24ead334665"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    final_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    weather_data = requests.get(final_url).json()
    return weather_data['main']


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot('location')
        temperature = Weather(city)['temp']
        response = "The current temperature at {} is {} degree Celsius.".format(city, temperature)
        dispatcher.utter_message(response)

        return [SlotSet('location', city)]
