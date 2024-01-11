import re
import response_dataset as res
from tools import pifi, Bot_log, Get_date, Get_time

def calculate_probability(
    user_input, targeted_words, high_priority=False, required_words=[]
):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_input:
        if word in targeted_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(targeted_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_input:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or high_priority:
        return int(percentage * 100)
    else:
        return 0


def verify_match(user_input):
    match_probability = {}

    def response(bot_response, targeted_words, high_priority=False, required_words=[]):
        nonlocal match_probability
        match_probability[bot_response] = calculate_probability(
            user_input, targeted_words, high_priority, required_words
        )

        """
                        ____
                       / __ \___  _________  ____  ____  ________
                      / /_/ / _ \/ ___/ __ \/ __ \/ __ \/ ___/ _ \
                     / _, _/  __(__  ) /_/ / /_/ / / / (__  )  __/
                    /_/ |_|\___/____/ .___/\____/_/ /_/____/\___/
                                    /_/

        """

    response(
        res.greetings_responses(),
        ["hello", "hi", "hey", "sup", "heyo"],
        high_priority=True,
    )
    response(
        res.farewells_responses(),
        [
            "bye",
            "goodbye",
        ],
        high_priority=True,
    )
    response(
        "I'm doing fine, and you?",
        ["how", "are", "you", "doing"],
        required_words=["how"]
    )
    response("You're welcome!", ["thank", "thanks"], high_priority=True)
    response(
        "Thank you!", ["i", "love", "code", "palace"], required_words=["code", "palace"]
    )
    response(
        res.general_info_responses(),
        [
            "college" ,"offer", "paper"
        ]
    )
    response(
        f"time now is {Get_time()} ",["time","now"]
    )

    best_match = max(match_probability, key=match_probability.get)
    return res.unknown() if match_probability[best_match] < 1 else best_match


def Bot_response(user_input):
    split_message = re.split(r"\s+|[,;?!.-]\s*", user_input.lower())
    response = verify_match(split_message)
    return response


def Start_chat(log = False):
    if log:
        pifi("Chat Bot")
        while True:
            user_input = input("You: ")
            response = Bot_response(user_input)
            print("Bot: " + response)
            Bot_log(user_input,response,Get_date(),Get_time())
    else:
        pifi("Chat Bot")
        while True:
            print("Bot: " + Bot_response(input("You: ")))