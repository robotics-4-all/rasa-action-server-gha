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

class Actionaskform1formcityslot(Action):

    def name(self) -> Text:
        return "action_ask_form1_form_city_slot"

    def run(self, dispatcher, tracker, domain):
        output = []

        dispatcher.utter_message(text = f"For which city?")

        return output

class Actionaskform1formtimeslot(Action):

    def name(self) -> Text:
        return "action_ask_form1_form_time_slot"

    def run(self, dispatcher, tracker, domain):
        output = []

        dispatcher.utter_message(text = f"For when?")

        return output


class Validateform1form(FormValidationAction):

    def name(self) -> Text:
        return "validate_form1_form"

    def extract_answer(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        if requested_slot == "answer":
            answer = None
            response = requests.get(f"r4a.issel.ee.auth.gr:8080/weather",
                headers = {},
                params = {}
            )
            try:
                answer = response.json()['weather']['forecast']
                output["answer"] = answer
            except:
                print(f'Error retrieving response from r4a.issel.ee.auth.gr:8080/weather with code {response.status_code}.')
        return output

class Actionanswerback(Action):

    def name(self) -> Text:
        return "action_answer_back"

    def run(self, dispatcher, tracker, domain):
        answer = tracker.get_slot('answer')
        NAME = compute_user_properties("NAME")
        CITY = compute_user_properties("CITY")
        output = []

        dispatcher.utter_message(text = f"Dear { NAME } the weather in { CITY } is { answer }")

        return output

class Actionresp(Action):

    def name(self) -> Text:
        return "action_resp"

    def run(self, dispatcher, tracker, domain):
        output = []

        dispatcher.utter_message(text = f"Hello friend")

        return output

