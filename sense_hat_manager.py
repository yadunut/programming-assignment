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

# Shows battery level on the display
def show_battery_level(battery):
    battery_pixels = int(math.floor(battery / 2))
    pixels_list = [green for x in range(battery_pixels)]
    pixels_list.append(blue if int(battery) % 2 == 1 else nothing)
    pixels_list += [nothing for x in range(64 - len(pixels_list))]
    sense.set_pixels(pixels_list)
    return pixels_list

def get_current_temperature():
    return sense.get_temperature()

# Where status is a list of the current pitch, roll, yaw

def get_cumulative_movement(status):
    curr_orientation = list(sense.get_orientation())
    """
    A very Interesting function where first, it will return a list of the differences between current orientation and status,
    then add the elements in the list and will return True if its greater than 20 or it will return False
    """
    result = True if sum(list(map(lambda x, y: abs(x - y), curr_orientation, status))) > 20 else False

    return result, curr_orientation

def sense_hat_main(battery):
    counter = 0
    status = [0, 0, 0]
    initial_temperature = get_current_temperature()
    distance_travelled = 0
    while counter < 5:
        time.sleep(3)
        counter += 1
        show_battery_level(battery)
        temperature_diff = temperature - initial_temperature
        is_moving, status = get_cumulative_movement(status)
        if(not is_moving):
            battery -= 1
        elif (is_moving and temperature_diff > 0.05):
            battery += 1
            distance_travelled += 0.01
    return battery, distance_travelled
