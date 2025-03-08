from Smart_Home_System import *



help = """ Sir You can:\n
    turn on or off the lights\n
    turn on or off speaker and set volume of speaker\n
    turn on or off tv and set volume of tv and also set timer for tv\n
    turn on or off ac and set temperature of ac and also set timer for ac\n
    exit to exit the system.
    """

def interact():
    print("Welcome to the Smart Home System!")
    while True:
        user = input("Command: ").strip().lower()
        if user == "exit":
            break
        elif user == "help":
            print(help)
        elif user == "turn on lights":
            light = ConcreteSmartLight()
            light.turn_on()
        elif user == "turn off lights":
            light = ConcreteSmartLight()
            light.turn_off()
        elif user == "turn on speaker":
            speaker = ConcreteSmartSpeaker()
            speaker.turn_on()
        elif user == "turn off speaker":
            speaker = ConcreteSmartSpeaker()
            speaker.turn_off()
        elif user == "set volume speaker":
            speaker = ConcreteSmartSpeaker()
            speaker.set_volume()
        elif user == "turn on tv":
            tv = ConcreteSmartTV()
            tv.turn_on()
        elif user == "turn off tv":
            tv = ConcreteSmartTV()
            tv.turn_off()
        elif user == "set volume tv":
            tv = ConcreteSmartTV()
            tv.set_volume()
        elif user == "set timer tv":
            tv = ConcreteSmartTV()
            tv.set_timer()
        elif user == "turn on ac":
            ac = ConcreteSmartAC()
            ac.turn_on()
        elif user == "turn off ac":
            ac = ConcreteSmartAC()
            ac.turn_off()
        elif user == "set temperature of ac":
            ac = ConcreteSmartAC()
            ac.set_temperature()
        elif user == "set timer of ac":
            ac = ConcreteSmartAC()
            ac.set_timer()
        else:
            print("Invalid command")


interact()
