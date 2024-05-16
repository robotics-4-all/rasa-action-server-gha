
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


class Actionaskcourseinfoformformcourseslot(Action):

    def name(self) -> Text:
        return "action_ask_course_info_form_form_course_slot"

    def run(self, dispatcher, tracker, domain):

        output = []


         
        dispatcher.utter_message(text = f"Which course do you need information about?")

        return output


class Validatecourseinfoformform(FormValidationAction):

    def name(self) -> Text:
        return "validate_course_info_form_form"

    def extract_info(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        course_slot = tracker.get_slot('course_slot')
        info = tracker.get_slot('info')
        if course_slot != None and info == None:
            course_slot = tracker.get_slot('course_slot')
            try:
                response = requests.get(f"https://university-api.edu/course/info",
                    headers = {},
                    params = {'course': f"{course_slot}"}
                )
                info = response.json()['details']
                output["info"] = info
            except:
                print(f'Error retrieving response from https://university-api.edu/course/info with code {response.status_code}.')
                dispatcher.utter_message(text = "Apologies, something went wrong.")
        return output

class Actionprovidecourseinfo(Action):

    def name(self) -> Text:
        return "action_provide_course_info"

    def run(self, dispatcher, tracker, domain):

        output = []

        info = tracker.get_slot('info')
        course_slot = tracker.get_slot('course_slot')

         
        dispatcher.utter_message(text = f"The information for the  { course_slot }  course is:  { info }")

        output.append(SlotSet('course_slot', None))
        output.append(SlotSet('info', None))
        return output

class Actionaskcourseregisterformformcourseslot(Action):

    def name(self) -> Text:
        return "action_ask_course_register_form_form_course_slot"

    def run(self, dispatcher, tracker, domain):

        output = []


         
        dispatcher.utter_message(text = f"Which course do you want to register for?")

        return output


class Validatecourseregisterformform(FormValidationAction):

    def name(self) -> Text:
        return "validate_course_register_form_form"

    def extract_confirmation(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        course_slot = tracker.get_slot('course_slot')
        confirmation = tracker.get_slot('confirmation')
        if course_slot != None and confirmation == None:
            course_slot = tracker.get_slot('course_slot')
            try:
                response = requests.post(f"https://university-api.edu/course/register",
                    headers = {},
                    data = {'course': f"{course_slot}"},
                    params = {}
                )
                confirmation = response.json()['status']
                output["confirmation"] = confirmation
            except:
                print(f'Error retrieving response from https://university-api.edu/course/register with code {response.status_code}.')
                dispatcher.utter_message(text = "Apologies, something went wrong.")
        return output

class Actionconfirmregistration(Action):

    def name(self) -> Text:
        return "action_confirm_registration"

    def run(self, dispatcher, tracker, domain):

        output = []

        confirmation = tracker.get_slot('confirmation')
        course_slot = tracker.get_slot('course_slot')

         
        dispatcher.utter_message(text = f"You have been registered for the  { course_slot }  course. Status:  { confirmation }")

        output.append(SlotSet('course_slot', None))
        output.append(SlotSet('confirmation', None))
        return output

class Actionaskappointmentformformfacultyslot(Action):

    def name(self) -> Text:
        return "action_ask_appointment_form_form_faculty_slot"

    def run(self, dispatcher, tracker, domain):

        output = []


         
        dispatcher.utter_message(text = f"Which faculty member would you like to meet?")

        return output


class Validateappointmentformform(FormValidationAction):

    def name(self) -> Text:
        return "validate_appointment_form_form"

    def extract_confirmation(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        faculty_slot = tracker.get_slot('faculty_slot')
        confirmation = tracker.get_slot('confirmation')
        if faculty_slot != None and confirmation == None:
            faculty_slot = tracker.get_slot('faculty_slot')
            try:
                response = requests.post(f"https://university-api.edu/faculty/appointment",
                    headers = {},
                    data = {'faculty': f"{faculty_slot}"},
                    params = {}
                )
                confirmation = response.json()['status']
                output["confirmation"] = confirmation
            except:
                print(f'Error retrieving response from https://university-api.edu/faculty/appointment with code {response.status_code}.')
                dispatcher.utter_message(text = "Apologies, something went wrong.")
        return output

class Actionconfirmappointment(Action):

    def name(self) -> Text:
        return "action_confirm_appointment"

    def run(self, dispatcher, tracker, domain):

        output = []

        faculty_slot = tracker.get_slot('faculty_slot')
        confirmation = tracker.get_slot('confirmation')

         
        dispatcher.utter_message(text = f"Your appointment with  { faculty_slot }  has been scheduled. Status:  { confirmation }")

        output.append(SlotSet('faculty_slot', None))
        output.append(SlotSet('confirmation', None))
        return output

class Actionaskeventinfoformformeventslot(Action):

    def name(self) -> Text:
        return "action_ask_event_info_form_form_event_slot"

    def run(self, dispatcher, tracker, domain):

        output = []


         
        dispatcher.utter_message(text = f"Which event do you need information about?")

        return output


class Validateeventinfoformform(FormValidationAction):

    def name(self) -> Text:
        return "validate_event_info_form_form"

    def extract_info(self, dispatcher, tracker, domain):
        output = {}
        requested_slot = tracker.get_slot('requested_slot')
        event_slot = tracker.get_slot('event_slot')
        info = tracker.get_slot('info')
        if event_slot != None and info == None:
            event_slot = tracker.get_slot('event_slot')
            try:
                response = requests.get(f"https://university-api.edu/event/info",
                    headers = {},
                    params = {'event': f"{event_slot}"}
                )
                info = response.json()['details']
                output["info"] = info
            except:
                print(f'Error retrieving response from https://university-api.edu/event/info with code {response.status_code}.')
                dispatcher.utter_message(text = "Apologies, something went wrong.")
        return output

class Actionprovideeventinfo(Action):

    def name(self) -> Text:
        return "action_provide_event_info"

    def run(self, dispatcher, tracker, domain):

        output = []

        event_slot = tracker.get_slot('event_slot')
        info = tracker.get_slot('info')

         
        dispatcher.utter_message(text = f"The information for the  { event_slot }  event is:  { info }")

        output.append(SlotSet('event_slot', None))
        output.append(SlotSet('info', None))
        return output

class Actiongreetback(Action):

    def name(self) -> Text:
        return "action_greet_back"

    def run(self, dispatcher, tracker, domain):

        output = []


         
        dispatcher.utter_message(text = f"Hello! How can I assist you today?")

        return output

