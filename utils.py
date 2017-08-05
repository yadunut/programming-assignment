import re
from classes import *
from strings import *
#Returns true if the regex is matched, else it will return false
def match_regex(regex_string, string):
    return True if (re.match(regex_string, string)) else False

# Finds a bike for you using the bike_no
def find_bike(bicycles, bike_no):
    bikes = list(filter(lambda x: x.bike_no == bike_no, bicycles))
    bike = bikes[0] if len(bikes) != 0 else None
    return bike
