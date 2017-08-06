from strings import *
from classes import *
from options import *

# User Option numbers and their meanings
QUIT_PROGRAM_NO= 0
READ_BICYCLE_INFO_NO = 1
DISPLAY_WITH_SERVICE_INFO_NO = 2
DISPLAY_SELECTED_BIKE_INFO_NO = 3
ADD_BICYCLE_NO = 4
DO_BICYCLE_MAINTENANCE_NO = 5
RIDE_A_BIKE_NO = 6
# A global State, keeps track of all the global variables such as the name of files, the list of bicycles, and whether it read the file
STATE = {
'bicycle_file_name': '',
'rides_file_name': '',
'bicycles': [],
'did_read_file': False
}
# Function to ask for the file names
def ask_for_file_names():
    print_data1_directory()
    bicycle_file_name = input(PROMPT_BICYCLE_FILE_NAME)
    print_data2_directory()
    rides_file_name = input(PROMPT_RIDE_FILE_NAME)
    return bicycle_file_name, rides_file_name

# Function to update the state
def update_state():
    global STATE
    # If I havent read the file or file name is wrong, it will ask for user input
    if not STATE['bicycle_file_name'] or not STATE['rides_file_name']:
        try:
            bicycle_file_name, rides_file_name = ask_for_file_names()
            STATE['bicycle_file_name'] = bicycle_file_name
            STATE['rides_file_name'] = rides_file_name
            STATE['bicycles'] = read_files(STATE)
            STATE['did_read_file'] = True
        except (NameError, FileNotFoundError) as e:
            print(str(e))
            STATE['bicycle_file_name'] = ""
            STATE['rides_file_name'] = ""
            STATE['did_read_file'] = False
            return update_state()
    # If i Havent read the file, It will try to update_state
    elif not STATE['did_read_file']:
        try:
            STATE['bicycles'] = read_files(STATE)
            STATE['did_read_file'] = True
        except (NameError, FileNotFoundError) as e:
            print(str(e))
            STATE['bicycle_file_name'] = ""
            STATE['rides_file_name'] = ""
            STATE['did_read_file'] = False
            print("STATE ERROR SETTING FALSE")
            return update_state()

# Function to call apppropriate method depending on user inputs
def choose_option(user_input):
    global STATE
    # Self Explanatory, Quits program
    if (user_input == QUIT_PROGRAM_NO):
        print(OPTIONS[QUIT_PROGRAM_NO])
        quit()

    elif (user_input == READ_BICYCLE_INFO_NO):
        print(OPTIONS[READ_BICYCLE_INFO_NO])
        update_state()
        read_bicycle_info(STATE)

    elif (user_input == DISPLAY_WITH_SERVICE_INFO_NO):
        print(OPTIONS[DISPLAY_WITH_SERVICE_INFO_NO])
        update_state()
        display_with_service_info(STATE)

    elif (user_input == DISPLAY_SELECTED_BIKE_INFO_NO):
        print(OPTIONS[DISPLAY_SELECTED_BIKE_INFO_NO])
        update_state()
        display_selected_bike_info(STATE)

    elif (user_input == ADD_BICYCLE_NO):
        print(OPTIONS[ADD_BICYCLE_NO])
        update_state()
        STATE['bicycles'] = add_cycle(STATE)
        write_bicycle_file(STATE)
        STATE['did_read_file'] = False

    elif (user_input == DO_BICYCLE_MAINTENANCE_NO):
        print(OPTIONS[DO_BICYCLE_MAINTENANCE_NO])
        update_state()
        STATE['bicycles'] = do_bicycle_maintenance(STATE)
        write_bicycle_file(STATE)
        STATE['did_read_file'] = False


    elif (user_input == RIDE_A_BIKE_NO):
        print(OPTIONS[RIDE_A_BIKE_NO])
        update_state()
        ride = ride_a_bike(STATE)
        write_ride_file(ride)
    else:
        raise InvalidInputException(ERROR_INPUT_WRONG)

def main():
    while True:
        print(MENU)
        try:
            user_input = int(input(PROMPT_ENTER_OPTION))
            choose_option(user_input)
        except ValueError as e:
            print(ERROR_INPUT_WRONG)
            return
        except InvalidInputException as e:
            print(str(e))
main()
