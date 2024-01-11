import random
from tools import get_time_period as current_time

# Bot Responses


# Greetings
def greetings_responses():
    return [
        f"Good {current_time().capitalize()}! How can I help you today?",
        "Hello! How can I assist you today?",
        "Hi there! What information are you looking for?",
        "Hey! I'm here to help. What do you need?",
        "Hello! Welcome to the college information bot. How can I help you?",
        "Hi! Feel free to ask me anything about the college.",
    ][random.randrange(5)]


def farewells_responses():
    return [
        "See you! If you have more questions, feel free to ask.",
        "Goodbye! Have a great day!",
        "Until next time! If you need assistance later, don't hesitate to return.",
        "Take care! If you need further information, just ask.",
    ][random.randrange(4)]


def general_info_responses():
    return [
        "Our college offers a variety of undergraduate and postgraduate programs in technology, management, and more.",
        "The college has multiple campuses. You can find information about them on the official website.",
        "To access your timetable, visit the college portal and log in with your credentials.",
        "For information on past year question papers (PYQ), check the examination section on the college website.",
    ][random.randrange(4)]


def unknown():
    return [
        "Could you please re-phrase that? ",
        "...",
        "Sounds about right.",
        "What does that mean?",
    ][random.randrange(4)]
