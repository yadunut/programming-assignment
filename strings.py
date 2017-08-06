MENU = \
"""

============================================================================================================
ADMIN MENU
==========
[1] Read bicycle info from file
[2] Display all bicycle info with servicing indication
[3] Display selected bicycle info
[4] Add a bicycle
[5] Perform bicycle maintenance
RIDER MENU
==========
[6]  Ride a bicycle
[0]  Exit
"""
PROMPT_ENTER_OPTION = "Enter your option: "
PROMPT_BICYCLE_FILE_NAME = "Enter Bicycle Data File Name: "
PROMPT_RIDE_FILE_NAME = "Enter Rides Data File Name: "

BICYCLE_FILE_HEADER = "Bike No.,Purchase Date,Batt %,Last Maintenance,KM since Last\n"
RIDE_FILE_HEADER = "Bike No.,Ride duration,Ride distance,Battery % \n"

OPTIONS = [
        "Option 0: Quit",
        "Option 1: Read bicycle info from file",
        "Option 2: Display all bicycle info with servicing indication",
        "Option 3: Display selected bicycle info",
        "Option 4: Add a bicycle",
        "Option 5: Perform bicycle maintenance",
        "Option 6: Ride a bicycle"
        ]

OPTION_2_HEADER = \
"""
Bike No.  Purchase Date  Batt %  Last Maintenance  KM since Last  Service?
--------  -------------  ------  ----------------  -------------  -------- \
"""
OPTION_2_FORMAT = "{:<10}{:<15}{:<8}{:<18}{:<15}{:<8}"

OPTION_3_HEADER = \
"""
Bike No.  Ride duration  Ride distance  Battery %
--------  -------------  -------------  --------- \
"""
OPTION_3_FORMAT = "{:<10}{:<15}{:<15}{:<9}"

OPTION_5_HEADER = \
"""
Bike No.  Batt %  Last Maintenance  KM since Last  Reason/s
--------  ------  ----------------  -------------  -------- \
"""
OPTION_5_FORMAT = "{:<10}{:<8}{:<18}{:<15}{:<8}"

OPTION_6_HEADER = \
"""
Bike No.  Batt %  KM since Last
--------  ------  ------------- \
"""
OPTION_6_FORMAT = "{:<10}{:<8}{:<15}"

OPTION_6_HEADER_2 = \
"""
Pitch  Roll  Yaw  Movement  Temp  Batt %  KM
-----  ----  ---  --------  ----  ------  ---- \
"""
OPTION_6_FORMAT_2 = "{:<7}{:<6}{:<5}{:<10}{:<6}{:<8}{:<4}"

PRINT_DATA1_DIRECTORY = \
"""
CSV Files in Current DATA1 DIRECTORY
------------------------------------ \
"""
PRINT_DATA2_DIRECTORY = \
"""
CSV Files in Current DATA2 DIRECTORY
------------------------------------ \
"""

ERROR_INPUT_WRONG = "You've entered a invalid input. Please enter number between 0-6"
ERROR_BIKE_NOT_FOUND = "The bicycle you've entered doesn't exist. Please Try again. Type 'cancel' to exit"
ERROR_RIDES_NOT_FOUND = "The bicycle you've entered doesn't have any rides. Please Try again. Type 'cancel' to exit"
ERROR_BIKE_ALREADY_EXIST = "The bicycle number you've entered already exists. Please Try Again. Type 'cancel' to exit"
ERROR_BIKE_NO_SERVICE = "The bicycle is not due for servicing. Please Try Again. Type 'cancel' to exit"
ERROR_BIKE_NEEDS_SERVICING = "Bicycle needs to be serviced. Cannot be rented at this time. Please Try Again. Type 'cancel' to exit"
