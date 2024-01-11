import os
import json
import pyfiglet
from datetime import datetime


def pifi(text):
    print(pyfiglet.figlet_format(text, font="slant"))
    
def Get_time():
    return datetime.now().strftime("%H:%M:%S")
def Get_date():
    return datetime.now().strftime("%d/%m/%Y")

def get_time_period():
    current_time = datetime.now().time()

    if (
        current_time >= datetime.strptime("00:00", "%H:%M").time()
        and current_time < datetime.strptime("12:00", "%H:%M").time()
    ):
        return "morning"
    elif (
        current_time >= datetime.strptime("12:00", "%H:%M").time()
        and current_time < datetime.strptime("17:00", "%H:%M").time()
    ):
        return "afternoon"
    elif (
        current_time >= datetime.strptime("17:00", "%H:%M").time()
        and current_time < datetime.strptime("20:00", "%H:%M").time()
    ):
        return "evening"
    else:
        return "night"

def Bot_log(*chat_data):
    #if the file is not present it will create a new file and add header to it
    if not os.path.isfile("chat_log.json"):
        with open("chat_log.json","w") as file:
            file.write('[\n]')
    #opening the file in read mode
    with open("chat_log.json","r") as file:
        #loading the data from the file
        data = json.load(file)
        #appending the new data to the file
        data.append({"user_input":chat_data[0],"bot_response":chat_data[1],"date":chat_data[2],"time":chat_data[3]})
    #opening the file in write mode
    with open("chat_log.json","w") as file:
        #writing the data to the file
        json.dump(data,file,indent=4)
