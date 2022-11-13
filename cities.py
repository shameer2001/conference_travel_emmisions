from typing import Dict, List, Tuple
from math import asin, sin, cos, sqrt

class City:
    def __init__(self, city, country, attendee_num, latitude, longitude):
        self.city = city
        self.country = country
        self.attendee_num = attendee_num #number of attendees
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


        if type(longitude) != float:
            raise ValueError("Longitude must be a float") 
        if type(latitude) != float:
            raise ValueError("Latitude must be a float") 





    
    def distance_to(self, other: 'City') -> float:
        '''use Haversine formula to calculate distance between 2 cities'''

        R=6371 #radius of earth
        first_term = sin(other.latitude/2  -  self.latitude/2)**2 #first term in equation
        second_term = cos(self.latitude)*cos(other.latitude)*( sin(other.longitude - self.longitude)**2 ) #second term in equation

        d = 2*R*asin(sqrt(  first_term + second_term   )) #distance 

        return d
    


    def co2_to(self, other: 'City') -> float:
        '''co2 released to travel from one city (`self`) to host city (`other`)'''
        distance_between_cities = self.distance_to(other)


        if distance_between_cities <= 1000: #public transport
            return 200*distance_between_cities*self.attendee_num

        elif distance_between_cities <=8000: #short-haul flight
            return 250*distance_between_cities*self.attendee_num

        else: #long-haul flight
            return 300*distance_between_cities*self.attendee_num           

 
class CityCollection:
    def __init__(self, cities):
        self.cities = cities
        
        if type(cities) != list:
            raise ValueError("Input must be a list of `City` objects")


    def countries(self) -> List[str]:
        countries = set([i.country for i in self.cities]) #a set only extracts unique values (countries in this case)
        
        return list(countries)

    def total_attendees(self) -> int:
        return sum( [i.attendee_num for i in self.cities] )
        
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

