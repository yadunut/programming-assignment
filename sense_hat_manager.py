from sense_hat import SenseHat
import math
import time
sense = SenseHat()

# DIfferent Colors I can use
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
nothing = (0, 0, 0)
# Shows battery level

def show_battery_level(battery):
    battery_pixels = int(math.floor(battery / 2))
    pixels_list = [green for x in range(battery_pixels)]
    pixels_list.append(blue if int(battery) % 2 == 1 else nothing)
    pixels_list += [nothing for x in range(64 - len(pixels_list))]
    sense.set_pixels(pixels_list)
    return pixels_list

def get_current_temperature():
    return sense.get_temperature()

def sense_hat_main(battery):
    counter = 0
    while counter < 5:
        time.sleep(3)
        counter += 1
        show_battery_level(battery)
        temperature = get_current_temperature()
