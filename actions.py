
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRestaurantSearch(Action):

    def name(self):
        return "action_restaurant_search"

    def run(self, dispatcher,tracker,domain):
        print('Value at food_type ' + tracker.get_slot('food_type'))
        print('Value at location name ' + tracker.get_slot('location_name'))

        dispatcher.utter_template('utter_restaurantdetails',tracker,restaurantname="Hello World")
        return []
