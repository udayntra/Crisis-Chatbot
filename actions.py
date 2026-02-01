from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideShelter(Action):
    def name(self) -> Text:
        return "action_provide_shelter"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = tracker.get_slot("location")

        if location:
            dispatcher.utter_message(text=f"The nearest emergency shelter in {location} is the central community hall. Please proceed safely.")
        else:
            dispatcher.utter_message(text="Please share your location so I can find the nearest shelter.")

        return []


class ActionEscalateEmergency(Action):
    def name(self) -> Text:
        return "action_escalate_emergency"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="This appears to be a high-risk situation. Contact emergency services immediately or dial your local emergency number.")
        return []
