from pyowm import OWM
from colorama import Fore, Back
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Russian
owm = OWM('97deaf0b7a4ebb9fbe0dee1a1be04b04', config_dict)
mgr = owm.weather_manager()
place = input("Type place?: ")

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(place)
w = observation.weather
print(Back.CYAN, Fore.BLACK)
print("В городе " + place + " сейчас " + w.detailed_status)
print("температура воздуха: " + str(w.temperature('celsius')["temp"]) + " градусов")
print("относительная влажность воздуха " + str(w.humidity) + " %")
print("скорость ветра: " + str(w.wind()["speed"]) + " м/с")
print("направление ветра: " + str(w.wind()["deg"]) + " deg")

