from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu


names = ['elliot', 'alicia', 'tim']


def fetch_athlete_names():
    fetched_names = names 
    return fetched_names


def fetch_events(athlete_name):
    if athlete_name == 'elliot':
        print('doing your hair')
    elif athlete_name == 'alicia':
        print('beast')
    else:
        print('legend')        


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        super().__init__(**kwargs)

    def add_athlete(self):
        new_athlete = self.root.ids.textfield.text
        names.append(new_athlete)


    def generate_items(self):
        items = fetch_athlete_names()
        menu_items = [
            {
                "viewclass": "MDMenuItem",
                "text": item,
                "callback": self.menu_callback,
            }
            for item in items
        ]
        return menu_items


    def open_dropdown(self):
        built_items = self.generate_items()
        MDDropdownMenu(items=built_items, width_mult=3).open(self.root.ids.dropdownbutton)


    def menu_callback(self, *args):
        athlete_name = args[0]
        names.remove(athlete_name)     


if __name__ == "__main__":
    my_app = MainApp()
    my_app.run()