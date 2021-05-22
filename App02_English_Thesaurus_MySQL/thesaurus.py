import json
import mysql.connector
from difflib import get_close_matches



def get_meaning_from_database(str):
    con = mysql.connector.connect(
        user="ardit700_student",
        password="ardit700_student",
        host="108.167.140.122",
        database="ardit700_pm1database"
    )

    cursor = con.cursor()
    query = cursor.execute("select * from Dictionary where Expression = '%s'" % str)
    results = cursor.fetchall()

    meanings = []
    if results:
        for result in results:
            meanings.append(result[1])
    
    return meanings

def get_meaning(str):
    str = str.lower()

    meanings = get_meaning_from_database(str)

    if meanings:
        response = meanings
    else:
        response = "Not a valid word!!! Please double check."
    return response

def display_meaning(meaning):
    if type(meaning) == list:
        for item in meaning:
            print(" >> ", item)
    else:
        print(" >> ", meaning)

while True:
    str = input("Enter a word: ")
    output = get_meaning(str)

    display_meaning(output)
    #print("\n")