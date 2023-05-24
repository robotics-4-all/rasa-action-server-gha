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

class Actiongreetback(Action):

    def name(self) -> Text:
        return "action_greet_back"

    def run(self, dispatcher, tracker, domain):
        output = []

        dispatcher.utter_message(text = f"Hello there!!!")

        return output

class Actionrespondiambot(Action):

    def name(self) -> Text:
        return "action_respond_iambot"

    def run(self, dispatcher, tracker, domain):
        output = []

        dispatcher.utter_message(text = f"I am a bot, powered by dFlow and Rasa.")

        return output

class Actionaskform1formname(Action):

    def name(self) -> Text:
        return "action_ask_form1_form_name"

    def run(self, dispatcher, tracker, domain):
        output = []

        dispatcher.utter_message(text = f"What's your name?")

        return output

class Actionaskform1formage(Action):

    def name(self) -> Text:
        return "action_ask_form1_form_age"

    def run(self, dispatcher, tracker, domain):
        output = []

        dispatcher.utter_message(text = f"How old are you?")

        return output


class Validateform1form(FormValidationAction):

    def name(self) -> Text:
        return "validate_form1_form"

    def extract_age(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        if requested_slot == "age":
            age = None
            text = tracker.latest_message['text']
            numbers = re.findall("\d+", text)
            if len(numbers):
                age = int(numbers[0])
            output["age"] = age
        return output

class Actionanswerback(Action):

    def name(self) -> Text:
        return "action_answer_back"

    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot('name')
        output = []

        dispatcher.utter_message(text = f"Glad to meet you  { name }")

        return output

