
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted, SlotSet, Restarted, FollowupAction

import requests, re, json, random, socket
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
    if property.lower() == 'hostname':
        return socket.gethostname()
    if property.lower() == 'public_ip':
        try:
            return requests.get('https://api.ipify.org').content.decode('utf8')
        except:
            return "Could not resolve IP address"


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


class Validateform1form(FormValidationAction):

    def name(self) -> Text:
        return "validate_form1_form"

    def extract_answer(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        city_slot = tracker.get_slot('city_slot')
        answer = tracker.get_slot('answer')
        if city_slot != None and answer == None:
            city_slot = tracker.get_slot('city_slot')
            try:
                response = requests.get(f"http://services.issel.ee.auth.gr/general_information/weather_openweather",
                    headers = {'access_token': 'Q5eJZ8sSLEX6XNmOHyMlWagI'},
                    params = {'city': f"{city_slot}", 'language': 'English'}
                )
                answer = response.json()['description']
                output["answer"] = answer
            except:
                print(f'Error retrieving response from http://services.issel.ee.auth.gr/general_information/weather_openweather with code {response.status_code}.')
                dispatcher.utter_message(text = "Apologies, something went wrong.")
        return output

class Actionanswerback(Action):

    def name(self) -> Text:
        return "action_answer_back"

    def run(self, dispatcher, tracker, domain):

        output = []

        city_slot = tracker.get_slot('city_slot')
        answer = tracker.get_slot('answer')

         
        dispatcher.utter_message(text = f"The kairos gia tin  { city_slot }  is  { answer }")

        output.append(SlotSet('city_slot', None))
        output.append(SlotSet('answer', None))
        return output

class Actiongreetback(Action):

    def name(self) -> Text:
        return "action_greet_back"

    def run(self, dispatcher, tracker, domain):

        output = []


         
        dispatcher.utter_message(text = f"Hello ma man!!!")

        return output

class Actionrespondiambot(Action):

    def name(self) -> Text:
        return "action_respond_iambot"

    def run(self, dispatcher, tracker, domain):

        output = []


         
        dispatcher.utter_message(text = f"I am a boot, powered by dFlow and Rasa.")

        return output

