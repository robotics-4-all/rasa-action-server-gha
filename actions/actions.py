
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


class Actionaskaf1formslot1(Action):

    def name(self) -> Text:
        return "action_ask_AF1_form_slot1"

    def run(self, dispatcher, tracker, domain):

        output = []


         
        dispatcher.utter_message(text = f"Give parameter 1")

        return output

class Actionaskaf1formslot2(Action):

    def name(self) -> Text:
        return "action_ask_AF1_form_slot2"

    def run(self, dispatcher, tracker, domain):

        output = []


         
        dispatcher.utter_message(text = f"Give parameter 2")

        return output

class Actionaskaf1formslot3(Action):

    def name(self) -> Text:
        return "action_ask_AF1_form_slot3"

    def run(self, dispatcher, tracker, domain):

        output = []

        slot1 = tracker.get_slot('slot1')

         
        dispatcher.utter_message(text = f"Give parameter 3 you { slot1 }")

        return output


class Validateaf1form(FormValidationAction):

    def name(self) -> Text:
        return "validate_AF1_form"

    def extract_slot2(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        if requested_slot == "slot2":
            slot2 = None
            intent = tracker.latest_message.get("intent", {}).get("name")
            if intent == 'find_doctor':
                slot2 = f"'True'"
            if intent == 'external_1':
                slot2 = f"'False'"
            output["slot2"] = slot2
        return output

class Actionanswers(Action):

    def name(self) -> Text:
        return "action_answers"

    def run(self, dispatcher, tracker, domain):

        output = []

        slot1 = tracker.get_slot('slot1')

         
        dispatcher.utter_message(text = f"Hello { slot1 } how are you")

        output.append(SlotSet('slot1', None))
        output.append(SlotSet('slot2', None))
        output.append(SlotSet('slot3', None))
        return output

class Actionasksf1formslot1(Action):

    def name(self) -> Text:
        return "action_ask_SF1_form_slot1"

    def run(self, dispatcher, tracker, domain):

        output = []


         
        dispatcher.utter_message(text = f"Give parameter 1")

        return output


class Validatesf1form(FormValidationAction):

    def name(self) -> Text:
        return "validate_SF1_form"

    def extract_slot2(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        slot1 = tracker.get_slot('slot1')
        slot2 = tracker.get_slot('slot2')
        if slot1 != None and slot2 == None:
            slot1 = tracker.get_slot('slot1')
            username = f"mario"
            try:
                response = requests.post(f"r4a.issel.ee.auth.gr/{username}",
                    headers = {},
                    data = {},
                    params = {'city': {'a': f"{slot1}", 'b': '0'}}
                )
                slot2 = response.json()
                output["slot2"] = slot2
            except:
                print(f'Error retrieving response from r4a.issel.ee.auth.gr/{username} with code {response.status_code}.')
                dispatcher.utter_message(text = "Apologies, something went wrong.")
        return output

class Actionanswers2(Action):

    def name(self) -> Text:
        return "action_answers2"

    def run(self, dispatcher, tracker, domain):

        output = []

        slot1 = tracker.get_slot('slot1')

         
        dispatcher.utter_message(text = f"The weather is  { slot1 }")

         
         
         
        username = f"mario"
        try:
            response = requests.post(f"r4a.issel.ee.auth.gr/{username}",
                headers = {},
                data = {},
                params = {'city': f"{slot1}"}
            )
        except:
            print(f'Error retrieving response from r4a.issel.ee.auth.gr/{username} with code {response.status_code}.')
            dispatcher.utter_message(text = "Apologies, something went wrong.")

        output.append(SlotSet('slot1', None))
        output.append(SlotSet('slot2', None))
        return output

