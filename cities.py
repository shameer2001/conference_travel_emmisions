from typing import Dict, List, Tuple
from math import asin, sin, cos, sqrt

class City:
    def __init__(self, city, country, attendee_num, latitude, longitude):
        self.city = city
        self.country = country
        self.attendee_num = attendee_num
        self.latitude = latitude
        self.longitude = longitude



        #create errors to  check for valud values and types of properties:
        if attendee_num < 0:
            raise ValueError("Number of attendees is negative") 
        if type(attendee_num) != int:
            raise ValueError("Number of attendees must be an integer")


        if latitude > 90 or latitude < -90:
            raise ValueError("Latitude is invald; must be between (-90, 90)") 
        if longitude >180 or longitude <-180:
            raise ValueError("Longitude is invald; must be between (-180, 180)") 


        if type(longitude) != float or type(longitude) != int:
            raise ValueError("Longitude must be an integer or float") 
        if type(latitude) != float or type(latitude) != int:
            raise ValueError("Latitude must be an integer or float") 





    
    def distance_to(self, other: 'City') -> float:
        '''use Haversine formula to calculate distance between 2 cities'''

        R=6371 #radius of earth
        first_term = sin(other.latitude/2  -  self.latitude/2)**2 #first term in equation
        second_term = cos(self.latitude)*cos(other.latitude)*( sin(other.longitude - self.longitude)**2 ) #second term in equation

        d = 2*R*asin(sqrt(  first_term + second_term   )) #distance 

        return d
    


    def co2_to(self, other: 'City') -> float:
        raise NotImplementedError

class CityCollection:
    ...

    def countries(self) -> List[str]:
        raise NotImplementedError

    def total_attendees(self) -> int:
        raise NotImplementedError

    def total_distance_travel_to(self, city: City) -> float:
        raise NotImplementedError

    def travel_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def total_co2(self, city: City) -> float:
        raise NotImplementedError

    def co2_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def summary(self, city: City):
        raise NotImplementedError

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        raise NotImplementedError

    def plot_top_emitters(self, city: City, n: int, save: bool):
        raise NotImplementedError

