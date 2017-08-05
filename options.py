from fileIo import *
from classes import *
from strings import *
from utils import *
from datetime import datetime

# prints count of bicycle records
def read_bicycle_info(STATE):
    length_of_records = len(STATE['bicycles'])
    print ('Number of Bicycle Records Read {}'.format(length_of_records))
# Prints the bicycle info with servicing status
def display_with_service_info(STATE):
    bicycles = STATE['bicycles']
    print(OPTION_2_HEADER)
    for bike in bicycles:
        print(OPTION_2_FORMAT.format(bike.bike_no, bike.purchase_date, bike.battery, bike.last_maintenance, bike.km_since_last, bike.service))

# Displays the selected bicycle info
def display_selected_bike_info(STATE):
    bicycles = STATE['bicycles']
    bike_no = input("Enter a bike no: ")
    if bike_no == 'cancel':
        return
    try :
        bike = find_bike(bicycles, bike_no)
        if not bike:
            raise BikeErrorException(ERROR_BIKE_NOT_FOUND)
        if not bike.rides:
            raise BikeErrorException(ERROR_RIDES_NOT_FOUND)
        print(OPTION_3_HEADER)
        for ride in bike.rides:
            print(OPTION_3_FORMAT.format(ride.bike_no, ride.ride_duration, ride.ride_distance, ride.battery))
    except BikeErrorException as e:
        print(str(e))
        display_selected_bike_info(STATE)

# Adds cycle to the STATE
def add_cycle(STATE):
    bicycles = STATE['bicycles']
    bike_no = input("Enter a bike no: ")
    if bike_no == 'cancel':
        return bicycles
    try:
        bike = find_bike(bicycles, bike_no)
        if bike:
            raise BikeErrorException(ERROR_BIKE_ALREADY_EXIST)
    except BikeErrorException as e:
        print(str(e))
        add_cycle(STATE)
    purchase_date = input("Purchase Date: ")
    try:
        bike = Bicycle(bike_no, purchase_date, 100, datetime.strftime(datetime.now(), "%d/%m/%Y"), 0)
        bicycles.append(bike)
        return bicycles
    except BicycleClassException as e:
        print(e)
        add_cycle(STATE)

def do_bicycle_maintenance(STATE):
    bicycles = STATE['bicycles']
    print(OPTION_5_HEADER)
    for bike in bicycles:
        print(OPTION_5_FORMAT.format(bike.bike_no, bike.battery, bike.last_maintenance, bike.km_since_last, bike.str_reasons()))
    bike_no = input("Enter a bike no: ")
    if bike_no == 'cancel':
        return bicycles
    try:
        bike = find_bike(bicycles, bike_no)
        if not bike:
            raise BikeErrorException(ERROR_BIKE_NOT_FOUND)
        if bike.service == "N":
            raise BikeErrorException(ERROR_BIKE_NO_SERVICE)
        bike.battery = 100
        bike.km_since_last = 0
        bike.last_maintenance = datetime.strftime(datetime.now(), "%d/%m/%Y")
        print(f'Bicycles: {bicycles}')
        return bicycles
    except BikeErrorException as e:
        print(str(e))
        do_bicycle_maintenance(STATE)
