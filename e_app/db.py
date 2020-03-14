import sqlite3


class competition:
    def __init__(self, name, comp_id=0):
        self.name = name
        self.comp_id = comp_id


class event:
    def __init__(self, comp_id, event_name, first_place, second_place, third_place, event_id = 0):
        self.comp_id = comp_id
        self.event_name = event_name
        self.first_place = first_place
        self.second_place = second_place
        self.third_place = third_place 
        self.event_id = event_id


class database:    
    def __init__(self, db_file):
        self.db_file = db_file    

    def generate_database(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        with conn:
            
            c.execute("""CREATE TABLE competition (
                    comp_id INTEGER PRIMARY KEY,
                    name text
                    )""")

            c.execute("""Create Table event (
                    event_id INTEGER PRIMARY KEY,
                    comp_id integer,
                    event_name text, 
                    first_place real,
                    second_place real,
                    third_place real
            )""")
                    

    def insert_competition(self, name):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO competition (name) VALUES (:name)",
            {'name':name})
        return 

    def fetch_competitions(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        with conn:
            c.execute("SELECT * FROM competition")
            result = c.fetchall()
            return result

    def insert_event(self, comp_id, event_name, first_place, second_place, third_place):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO event (comp_id, event_name, first_place, second_place, third_place) VALUES (:comp_id, :event_name, :first_place, :second_place, :third_place)",
            {'comp_id':comp_id, 'event_name':event_name, 'first_place':first_place, 'second_place':second_place, 'third_place':third_place})
        return 

    def fetch_events(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        with conn:
            c.execute("SELECT * FROM event")
            result = c.fetchall()
            return result


db = database('db.db')
#db.generate_database()
#db.insert_competition('auckland champs')
#db.insert_event(1, '100m', 10.1, 10.2, 10.6)
#db.insert_event(1, '200m', 19.6, 19.7, 19.9)
#print(db.fetch_events())
