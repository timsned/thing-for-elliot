from db import db
import PySimpleGUI as sg

comps = db.fetch_competitions()
events = db.fetch_events()

def get_comps():
    return [item[1] for item in db.fetch_competitions()]

def get_events():
    event_list = []
    for event in db.fetch_events():
        if event[2] not in event_list:
            event_list.append(event[2])
    return event_list        


def get_comp_id(comp_name):
    for comp in comps:
        if comp[1] == comp_name:
            return comp[0]            

def get_event_placings(comp_id, event_name):
    for event in db.fetch_events():
        if event[1] == comp_id:
            if event[2] == event_name:
                return [event[3], event[4], event[5]]
  

competitions = get_comps()
events = get_events()


first_place = ''
second_place = ''
third_place = ''

while True:

    layout = [[sg.Text('Results')],
            [sg.Text('Competition'), sg.Combo(competitions)],
            [sg.Text('Enter event'), sg.Combo(events)],
            [sg.Text('First Place'), sg.Text(first_place)],
            [sg.Text('Second Place'), sg.Text(second_place)],
            [sg.Text('Third Place'), sg.Text(third_place)],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
    
    window = sg.Window('Window Title', layout)
    
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    comp_id = get_comp_id(values[0])
    placings = get_event_placings(comp_id, values[1])
    first_place = placings[0]
    second_place = placings[1]
    third_place = placings[2]
    

window.close()

