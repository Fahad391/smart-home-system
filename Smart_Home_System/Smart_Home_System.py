from abc import ABC, abstractmethod

class smart_Devise(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
    @abstractmethod
    def set_timer(self):
        pass
    @abstractmethod
    def set_volume(self):
        pass
    @abstractmethod
    def set_temperature(self):
        pass

class smart_Light(smart_Devise):
    def turn_on(self):
        print("Light turned on")
    def turn_off(self):
        print("Light turned off")

class smart_Speaker(smart_Devise):
    def turn_on(self):
        print("Speaker turned on")
    def turn_off(self):
        print("Speaker turned off")
    def set_volume(self):
        try:
            user = int(input("Enter volume level: "))
            if user > 100:
                print("Volume level should be less than 100")
            else:
                print("Volume set to", user)
        except ValueError:
            print("Enter a valid number\nnumber cannot be a string nor negative")
class smart_TV(smart_Devise):
    def turn_on(self):
        print("TV turned on")
    def turn_off(self):
        print("TV turned off")
    def set_volume(self):
        try:
            user = int(input("Enter volume level: "))
            if user > 100:
                print("Volume level should be less than 100")
            else:
                print("Volume set to", user)
        except ValueError:
            print("Enter a valid number\nnumber cannot be a string nor negative")
    def set_timer(self):
        try:
            user = int(input("Enter timer in minutes: "))
            print("Timer set to", user, "minutes")
        except ValueError:
            print("Enter a valid number\nnumber cannot be a string nor negative")
class smart_AC(smart_Devise):
    def turn_on(self):
        print("AC turned on")
    def turn_off(self):
        print("AC turned off")
    def set_timer(self):
        try:
            user = int(input("Enter timer in minutes: "))
            print("Timer set to", user, "minutes")
        except ValueError:
            print("Enter a valid number\nnumber cannot be a string nor negative")
    def set_temperature(self):
        try:
            user = int(input("Enter temperature: "))
            print("Temperature set to", user, "degree")
            if user > 30 or user < 16:
                print("Temperature is limited between 16 and 30 degree")
                
        except ValueError:
            print("Enter a valid number\nnumber cannot be a string nor negative")


class ConcreteSmartLight(smart_Light):
    def turn_on(self):
        return super().turn_on()
    def turn_off(self):
        return super().turn_off()
    
    def set_temperature(self):
        pass
    def set_timer(self):
        pass
    def set_volume(self):
        pass

class ConcreteSmartAC(smart_AC):
    def turn_on(self):
        return super().turn_on()
    def turn_off(self):
        return super().turn_off()
    def set_temperature(self):
        return super().set_temperature()
    def set_timer(self):
        return super().set_timer()
    def set_volume(self):
        pass
 
class ConcreteSmartSpeaker(smart_Speaker):
    def turn_on(self):
        return super().turn_on()
    def turn_off(self):
        return super().turn_off()
    def set_volume(self):
        return super().set_volume()
    def set_timer(self):
        pass
    def set_temperature(self):
        pass

class ConcreteSmartTV(smart_TV):
    def turn_on(self):
        return super().turn_on()
    def turn_off(self):
        return super().turn_off()
    def set_volume(self):
        return super().set_volume()
    def set_timer(self):
        return super().set_timer()
    def set_temperature(self):
        pass
