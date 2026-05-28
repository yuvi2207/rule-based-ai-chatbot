# Rule Based AI ChatBot

import datetime
import random

name = input("Enter your name : ")

currentHour = datetime.datetime.now().hour

if 5 <= currentHour < 12:
    print("Good Morning", name)
elif 12 <= currentHour < 17:
    print("Good Afternoon", name)
elif 17 <= currentHour < 21:
    print("Good Evening", name)
else:
    print("Good Night", name)

print("\nWelcome to AI ChatBot")
print("Type 'bye' to exit\n")


# chatbot responses
responses = {

    "hello": [
        "Hi there!",
        "Hello ",
        "Hey!"
    ],

    "how are you": [
        "I am fine",
        "Doing good "
    ],

    "who are you": [
        "I am a Python chatbot",
        "I am your AI friend"
    ],

    "motivate me": [
        "Never give up",
        "Practice makes perfect",
        "Keep learning daily "
    ],

    "python": [
        "Python is easy and powerful",
        "Python is good for beginners"
    ],

    "bye": [
        "Goodbye",
        "See you again"
    ]
}


# function for chatbot response
def getResponse(userText):

    userText = userText.lower()

    for key in responses:

        if key in userText:
            return random.choice(responses[key])

    return "Sorry, I don't understand that yet"


# chatbot loop
while True:

    userInput = input("You : ")

    answer = getResponse(userInput)

    print("Bot :", answer)

    if "bye" in userInput.lower():
        break