from strings import *
from classes import *
import os

# Prints the contents in data1 directory
def print_data1_directory():
    print(PRINT_DATA1_DIRECTORY)
    files = [f for f in os.listdir("./data1")]
    for f in files:
        if (str(f).endswith(".csv")):
            print(f)
    print()

# Prints the contents in data2 directory
def print_data2_directory():
    print(PRINT_DATA2_DIRECTORY)
    files = [f for f in os.listdir("./data2")]
    for f in files:
        if (str(f).endswith(".csv")):
            print(f)
    print()

def ask_file_name():
    print_data1_directory()
    bicycle_file_name = input(PROMPT_BICYCLE_FILE_NAME)
    print_data2_directory()
    rides_file_name = input(PROMPT_RIDE_FILE_NAME)
    return bicycle_file_name, rides_file_name

# Reads data file 1 and converts the data to a list of Bicycle Objects and returns it
def read_files(STATE):
    bicycles = []
    rides = []
    bicycle_file_path = "./data1/" + STATE['bicycle_file_name']
    rides_file_path = "./data2/" + STATE['rides_file_name']
    bike_file_object = open("./data1/" + STATE['bicycle_file_name'], "r")
    rides_file_object = open("./data2/" + STATE['rides_file_name'], "r")

    bike_file_object.readline()
    rides_file_object.readline()

    for data in rides_file_object.readlines():
        data_list = data.strip().split(",")
        ride = Ride(data_list[0], float(data_list[1]), float(data_list[2]), int(data_list[3]))
        rides.append(ride)

    for line in bike_file_object.readlines():
        data_list = line.strip().split(",")
        bike = Bicycle(data_list[0], data_list[1], int(data_list[2]), data_list[3], float(data_list[4]))
        bike.rides = list(filter(lambda x: x.bike_no == bike.bike_no, rides))
        bicycles.append(bike)
    bike_file_object.close()
    rides_file_object.close()
    return bicycles
# Updates the file with the updated state
def write_bicycle_file(STATE):
    bicycles = STATE['bicycles']
    bicycle_file_path = "./data1/" + STATE['bicycle_file_name']
    bike_file_object = open(bicycle_file_path, "w")
    bike_file_object.write(BICYCLE_FILE_HEADER)
    for bike in bicycles:
        bike_file_object.write(str(bike) + "\n")
# Writes the ride to the rides file
def write_ride_file(ride):
    rides_file_path = "./data2/" + STATE['rides_file_name']
    rides_file_object = open(rides_file_path, "a")
    rides_file_object.ride(str(ride) + "\n")
