import json
from difflib import get_close_matches

myData = json.load(open('data.json'))

def get_meaning(str):
    str = str.lower()
    if str in myData:
        response = myData.get(str)
    elif str.title() in myData:
        response = myData.get(str.title())
    elif str.upper() in myData:
        response = myData.get(str.upper())
    elif len(get_close_matches(str,myData.keys())) > 0:
        user_input = input("Do you mean %s instead. Enter Y if yes. N if no :" % get_close_matches(str,myData.keys())[0])
        if (user_input == 'Y'):
            response = myData.get(get_close_matches(str,myData.keys())[0])
        elif (user_input == 'N'):
            response = "Not a valid word!!! Please double check."  
        else:
            response = "Sorry!!! We do not understand your entry."
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