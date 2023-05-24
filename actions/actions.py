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

