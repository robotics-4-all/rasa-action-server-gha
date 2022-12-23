from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted, SlotSet, Restarted

import requests, re, json, random
from datetime import datetime

def compute_system_properties(property):
    if property.lower() == 'time':
      return datetime.now().strftime("%I:%M")
    if property.lower() == 'location':
      return ''
    if property.lower() == 'random_int':
      return random.randint(0,100)
    if property.lower() == 'random_float':
      return random.random()

def compute_user_properties(property):
    if property.lower() == 'name':
      return ''
    if property.lower() == 'surname':
      return ''
    if property.lower() == 'age':
      return ''
    if property.lower() == 'email':
      return ''
    if property.lower() == 'phone':
      return ''
    if property.lower() == 'city':
      return ''
    if property.lower() == 'address':
      return ''


class Validategiveweatherform(FormValidationAction):

    def name(self) -> Text:
        return "validate_give_weather_form"

    def extract_temperature_answer(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        if requested_slot == "temperature_answer":
            temperature_answer = None
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude=40.62&longitude=22.94&current_weather=true",
                headers = {},
                params = {}
            )
            try:
                temperature_answer = response.json()['current_weather']['temperature']
                output["temperature_answer"] = temperature_answer
            except:
                print(f'Error retrieving response from https://api.open-meteo.com/v1/forecast?latitude=40.62&longitude=22.94&current_weather=true with code {response.status_code}.')
        return output

    def extract_time_answer(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        if requested_slot == "time_answer":
            time_answer = None
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude=40.62&longitude=22.94&current_weather=true",
                headers = {},
                params = {}
            )
            try:
                time_answer = response.json()['current_weather']['time']
                output["time_answer"] = time_answer
            except:
                print(f'Error retrieving response from https://api.open-meteo.com/v1/forecast?latitude=40.62&longitude=22.94&current_weather=true with code {response.status_code}.')
        return output

class Actionanswerback(Action):

    def name(self) -> Text:
        return "action_answer_back"

    def run(self, dispatcher, tracker, domain):
        time_answer = tracker.get_slot('time_answer')
        temperature_answer = tracker.get_slot('temperature_answer')
        output = []

        dispatcher.utter_message(text = f"The weather is  { temperature_answer } at { time_answer }")

        return output

