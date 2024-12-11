import random

hellow = ["hi", "is anyone there?", "hello", "good day", "hello there"]
bye = ["cya", "see you later", "bye", "goodbye", "i am leaving", "have a good day"]
howare = ["how are you", "whats up", "how you doing"]
name = ["whats your name", "what is your name", "do you have any name", "what should i call you", "name"]
menu = ["i want to buy something", "what is on the menu", "what do you recommend?", "could i get something to eat"]
hours = ["when are you guys open", "what are your hours", "hours of operation", "time", "work time", "time period"]

print("*******************************************************\n")

while True:
    a = input('User said: ')
    
    if a.lower() in hellow:
        botans = ["Hello!", "hi", "hi there", "welcome"]
        print('Bot said: ' + random.choice(botans) + '\n')
    
    elif a.lower() in bye:
        botans = ["Sad to see you go :(", "Talk to you later", "Goodbye!", "Have a nice day"]
        print('Bot said: ' + random.choice(botans) + '\n')
    
    elif a.lower() in howare:
        botans = ["I am fine, thanks!", "Happy", "I am good"]
        print('Bot said: ' + random.choice(botans) + '\n')
    
    elif a.lower() in name:
        botans = ["My name is TVC bot", "You can call me TVC bot", "TVC Bot in your service", "My friends call me TVC Bot"]
        print('Bot said: ' + random.choice(botans) + '\n')
    
    elif a.lower() in menu:
        botans = ["We sell apples!", "Apples are on the menu!", "Please take a look at Apples"]
        print('Bot said: ' + random.choice(botans) + '\n')
    
    elif a.lower() in hours:
        botans = ["We are open 7am-4pm Monday-Friday!"]
        print('Bot said: ' + random.choice(botans) + '\n')
    
    else:
        print('Bot said: Sorry, what?\n')
