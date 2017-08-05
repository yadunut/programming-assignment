from datetime import datetime
from exceptions import *
from utils import *

# Class to store bicycle data
class Bicycle():
    def __init__(self, bike_no, purchase_date, battery, last_maintenance, km_since_last, rides = []):
        date_time = "%d/%m/%Y"
        # This class does all input validation and throws exceptions accordingly
        # Validation to ensure bike no is correct format
        if (match_regex("^T\d\d\d$", bike_no)):
            self.bike_no = bike_no
        else:
            raise BicycleClassException("Bike Number wrong format")

        # Makes sure purchase_date is entered in correct format
        try:
            datetime.strptime(purchase_date, date_time)
            self.purchase_date = purchase_date
        except ValueError:
            raise BicycleClassException("Purchase Date is wrong format")

        # Makes sure battery is correct format
        if (isinstance(battery, int)):
            self.battery = battery
        else:
            raise BicycleClassException("Battery is not int")

        # Makes sure last maintenance is correct format
        try:
            datetime.strptime(last_maintenance, date_time)
            self.last_maintenance = last_maintenance
        except ValueError:
            raise BicycleClassException("Last Maintenance is wrong format")

        # Makes sure km since last is correct format
        if (isinstance(km_since_last, float) or isinstance(km_since_last, int)):
            self.km_since_last = km_since_last
        else:
            raise BicycleClassException("Km Since Last is not float")

        self.rides = rides

        # Gets todays time and gets delta time (Time diff between today and last maintenance)
        today_object = datetime.now()
        maintenance_object = datetime.strptime(last_maintenance, date_time)
        delta = today_object - maintenance_object

        # Creates list of reasons
        reasons = []
        if (self.battery < 10):
            reasons.append("Batt")
        if (km_since_last > 50):
            reasons.append("KM")
        if (delta.days > 365 / 2):
            reasons.append("Months")
        self.reasons = reasons
        # Says if service is Needed
        self.service = "Y" if (len(reasons)) else "N"

        # returns the Bicycle object as a csv, for writing to files
    def __str__(self):
        return ("{},{},{},{},{}".format(self.bike_no, self.purchase_date, self.battery, self.last_maintenance, self.km_since_last))
    def str_reasons(self):
        if len(self.reasons) == 0:
            return ""
        elif len(self.reasons) == 1:
            return self.reasons[0]
        else:
            return " & ".join(self.reasons)

# Class to store ride data (File2)
class Ride():
    def __init__(self, bike_no, ride_duration, ride_distance, battery):
        # This class does all input validation and throws exceptions accordingly
        # Validation to ensure bike no is correct format
        if (match_regex("^T\d\d\d$", bike_no)):
            self.bike_no = bike_no
        else:
            raise RideClassException("Bike Number wrong format")

        # Validation to ensure ride duration is of proper format
        if (isinstance(ride_duration, float) or isinstance(ride_duration, int)):
            self.ride_duration = ride_duration
        else:
            raise RideClassException("Ride Duration isn't a number")

        # Validation to ensure ride distance is of proper format
        if (isinstance(ride_distance, float) or isinstance(ride_distance, int)):
            self.ride_distance = ride_distance
        else:
            raise RideClassException("Ride Distance isn't a number")

        # Makes sure battery is correct format
        if (isinstance(battery, int)):
            self.battery = battery
        else:
            raise BicycleClassException("Battery is not int")
    # Returns the ride data as CSV
    def __str__(self):
        return "{},{},{},{}".format(self.bike_no, self.ride_duration, self.ride_distance, self.battery)
