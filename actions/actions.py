
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



class Validateretrieveajokedlg1formform(FormValidationAction):

    def name(self) -> Text:
        return "validate_retrieveAJoke_dlg_1_form_form"

    def extract_question(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        question = tracker.get_slot('question')
        if question == None:
            try:
                response = requests.get(f"http://localhost:8800/quotes/get_joke",
                    headers = {},
                    params = {}
                )
                question = response.json()['question']
                output["question"] = question
            except:
                print(f'Error retrieving response from http://localhost:8800/quotes/get_joke with code {response.status_code}.')
                dispatcher.utter_message(text = "Apologies, something went wrong.")
        return output

    def extract_answer(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        question = tracker.get_slot('question')
        answer = tracker.get_slot('answer')
        if question != None and answer == None:
            question = tracker.get_slot('question')
            try:
                response = requests.get(f"http://localhost:8800/quotes/get_joke",
                    headers = {},
                    params = {}
                )
                answer = response.json()['answer']
                output["answer"] = answer
            except:
                print(f'Error retrieving response from http://localhost:8800/quotes/get_joke with code {response.status_code}.')
                dispatcher.utter_message(text = "Apologies, something went wrong.")
        return output

class Actionretrieveajokedlg1ag(Action):

    def name(self) -> Text:
        return "action_retrieveAJoke_dlg_1_ag"

    def run(self, dispatcher, tracker, domain):

        output = []

        question = tracker.get_slot('question')
        answer = tracker.get_slot('answer')

         
        dispatcher.utter_message(text = f"Here is a joke for you: Question: {question} Answer: {answer}")

        output.append(SlotSet('question', None))
        output.append(SlotSet('answer', None))
        return output

class Actionasktheweatherinformationdlg2formformcity(Action):

    def name(self) -> Text:
        return "action_ask_theWeatherInformation_dlg_2_form_form_city"

    def run(self, dispatcher, tracker, domain):

        output = []
        asked = 'city'
        output.append(SlotSet('asked', asked))
        
        dispatcher.utter_message(text = f"Please provide the city")

        return output


class Validatetheweatherinformationdlg2formform(FormValidationAction):

    def name(self) -> Text:
        return "validate_theWeatherInformation_dlg_2_form_form"
    
    def extract_city(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        city = tracker.get_slot('city')
        asked = tracker.get_slot('asked')
        if city == None and asked == 'city':
            city = tracker.latest_message.get("text")
            output["city"] = city
        return output


    def extract_description(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        city = tracker.get_slot('city')
        description = tracker.get_slot('description')
        if city != None and description == None:
            city = tracker.get_slot('city')
            try:
                response = requests.get(f"http://localhost:8800/weather_information",
                    headers = {},
                    params = {'city': f"{city}"}
                )
                print(response.json())
                description = response.json()['description']
                output["description"] = description
            except:
                print(f'Error retrieving response from http://localhost:8800/weather_information with code {response.status_code}.')
                dispatcher.utter_message(text = "Apologies, something went wrong.")
        return output

    def extract_temp(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        description = tracker.get_slot('description')
        temp = tracker.get_slot('temp')
        if description != None and temp == None:
            description = tracker.get_slot('description')
            city = tracker.get_slot('city')
            try:
                response = requests.get(f"http://localhost:8800/weather_information",
                    headers = {},
                    params = {'city': f"{city}"}
                )
                temp = response.json()['temp']
                print(response.json())
                output["temp"] = temp
            except:
                print(f'Error retrieving response from http://localhost:8800/weather_information with code {response.status_code}.')
                dispatcher.utter_message(text = "Apologies, something went wrong.")
        return output

class Actiontheweatherinformationdlg2ag(Action):

    def name(self) -> Text:
        return "action_theWeatherInformation_dlg_2_ag"

    def run(self, dispatcher, tracker, domain):

        output = []

        city = tracker.get_slot('city')
        description = tracker.get_slot('description')
        temp = tracker.get_slot('temp')
         
        dispatcher.utter_message(text = f"The weather in {city} is {description} with a temperature of {temp}.")

        output.append(SlotSet('city', None))
        output.append(SlotSet('description', None))
        output.append(SlotSet('temp', None))
        return output
    

class Validatethisshit(FormValidationAction):

    def name(self) -> Text:
        return "validate_storesANewNoteInPersonalFileRegistry_dlg_3_form_form"
    
    def extract_note(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        note = tracker.get_slot('note')
        asked = tracker.get_slot('asked')
        if note == None and asked == 'note':
            note = tracker.latest_message.get("text")
            output["note"] = note
        return output


class Actionaskstoresanewnoteinpersonalfileregistrydlg3formformnote(Action):

    def name(self) -> Text:
        return "action_ask_storesANewNoteInPersonalFileRegistry_dlg_3_form_form_note"

    def run(self, dispatcher, tracker, domain):

        output = []

        asked = 'note'
        output.append(SlotSet('asked', asked))
        
        dispatcher.utter_message(text = f"Please provide the note")

        return output

class Actionstoresanewnoteinpersonalfileregistrydlg3ag(Action):

    def name(self) -> Text:
        return "action_storesANewNoteInPersonalFileRegistry_dlg_3_ag"

    def run(self, dispatcher, tracker, domain):

        output = []

        note = tracker.get_slot('note')

         
         
        try:
            response = requests.post(f"http://localhost:8800/notes/add",
                headers = {'Content-Type': 'application/json', },
                data = {},
                params = {'note': f"{note}"}
            )
        except:
            print(f'Error retrieving response from http://localhost:8800/notes/add with code {response.status_code}.')
            dispatcher.utter_message(text = "Apologies, something went wrong.")

         
        dispatcher.utter_message(text = f"Your new note has been successfully stored in the personal file registry.")

        output.append(SlotSet('note', None))
        return output

