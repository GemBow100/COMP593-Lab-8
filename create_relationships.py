"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
from random import randint, choice
from faker import Faker


# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    # TODO: Function body
    # Hint: See example code in lab instructions entitled "Add the Relationships Table"
    
    con = sqlite3.connect(db_path)
    cur = con.cursor()
# SQL query that creates a table named 'relationships'.
    create_relationships_tbl_query = """
    CREATE TABLE IF NOT EXISTS relationships
    (
        id INTEGER PRIMARY KEY,
        person1_id INTEGER NOT NULL,
        person2_id INTEGER NOT NULL,
        type TEXT NOT NULL,
        start_date DATE NOT NULL,
        FOREIGN KEY (person1_id) REFERENCES people (id),
        FOREIGN KEY (person2_id) REFERENCES people (id)
    );
"""
    # Execute the SQL query to create the 'relationships' table.
    cur.execute(create_relationships_tbl_query)
    con.commit()
    con.close()


    return

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    # TODO: Function body
    # Hint: See example code in lab instructions entitled "Populate the Relationships Table"
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # SQL query that inserts a row of data in the relationships table.
    add_relationship_query = """
        INSERT INTO relationships
        (
            person1_id,
            person2_id,
            type,
            start_date
        )
            VALUES (?, ?, ?, ?);
    """
    fake = Faker("en_CA")
    for _ in range (100):
        # Randomly select first person in relationship
        person1_id = fake.random_int(min=1, max=200)
        # Randomly select second person in relationship
        # Loop ensures person will not be in a relationship with themself
        person2_id = fake.random_int(min= 1, max=200)
    
        while person2_id == person1_id:
                person2_id = randint(1, 200)
        # Randomly select a relationship type
        rel_type = choice(('friend', 'spouse', 'partner', 'relative'))
        # Randomly select a relationship start date between now and 50 years ago
        start_date = fake.date_between(start_date='-30y', end_date='today').strftime('%Y-%M-%D %H:%M:%S')
        # Create tuple of data for the new relationship
        new_relationship = (person1_id, person2_id, rel_type, start_date)
    
        # Add the new relationship to the DB
        cur.execute(add_relationship_query, new_relationship)
        con.commit()
    con.close()

    return 

if __name__ == '__main__':
   main()