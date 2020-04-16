from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.app import App
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import Screen



names = ['elliot', 'alicia', 'tim']    


class OurScreen(Screen):
    pass



class NamesDropdown(MDRaisedButton):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)


    def generate_items(self):
        items = names
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
        MDDropdownMenu(items=built_items, width_mult=3).open(self)


    def menu_callback(self, *args):
        athlete_name = args[0]
        self.app.name_selected = athlete_name   








class PrintNameButton(MDRaisedButton):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

    def print_name(self):
        if self.app.name_selected:
            print(self.app.name_selected)










class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.name_selected = None
        self.title = "My Material Application"
        super().__init__(**kwargs)

    
if __name__ == "__main__":
    my_app = MainApp()
    my_app.run()