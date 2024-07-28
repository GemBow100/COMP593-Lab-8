"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import sqlite3
from create_relationships import db_path, script_dir
import pandas as pd

def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(script_dir, 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    # TODO: Function body
    # Hint: See example code in lab instructions entitled "Get a List of Relationships"
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # SQL query to get all relationships
    all_relationships_query = """
        SELECT person1.name, person2.name, start_date, type FROM relationships
        JOIN people person1 ON person1_id = person1.id
        JOIN people person2 ON person2_id = person2.id;
"""
    # Execute the query and get all results
    cur.execute(all_relationships_query)
    all_relationships = cur.fetchall()
    con.close()
    #Print sentences describing each relationship
    for person1, person2, start_date, type in all_relationships:
        print(f'{person1} has been a {type} of {person2} since {start_date}.')

    return

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    # TODO: Function body
    # Hint: We did this in Lab 7.
    DataFramelist = [] 
    for person1, person2, start_date in married_couples:
        DataFramelist.append({'name1': person1,
                              'name2': person2,
                              'Anniversary': start_date
                              })
    
    df = pd.DataFrame(DataFramelist)

    df.to_csv(csv_path,'Married Couples.csv', index=False,)

    print(df)
    return

if __name__ == '__main__':
   main()