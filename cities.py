from typing import Dict, List, Tuple
from math import asin, sin, cos, sqrt, radians

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
        first_term = sin(radians(   other.latitude/2  -  self.latitude/2   ))**2 #first term in equation
        second_term = cos(radians(   self.latitude   ))*cos(radians(  other.latitude  ))*( sin(radians(  other.longitude - self.longitude  ))**2 ) #second term in equation

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
        distance_per_attendee = sum( [i.distance_to(city) for i in self.cities] )
        total_distance = distance_per_attendee*self.total_attendees()

        return total_distance




    def travel_by_country(self, city: City) -> Dict[str, float]:
        country_to_distance = {}
        keys = [str(i.country) for i in self.cities]
        values = [i.distance_to(city)*i.attendee_num for i in self.cities]


        #assign 0 to each key:        
        for i in range(len(keys)):
            country_to_distance[keys[i]] = 0 

        
        for i in range(len(keys)):   
            #if there is already a distance assigned to the country (ie >0 value), then
            # add on the new value to avoid replacing the value:

            if country_to_distance[keys[i]] >0:
                country_to_distance[keys[i]] = country_to_distance[keys[i]] + values[i]        
            else:
                country_to_distance[keys[i]] =  values[i]
                
            
                
        return country_to_distance





    def total_co2(self, city: City) -> float:
        co2_per_attendee = sum( [i.co2_to(city) for i in self.cities] )
        total_co2 = co2_per_attendee*self.total_attendees()

        return total_co2




    def co2_by_country(self, city: City) -> Dict[str, float]:
        country_to_co2 = {}
        keys = [str(i.country) for i in self.cities]
        values = [i.co2_to(city)*i.attendee_num for i in self.cities]
        

        
        for i in range(len(keys)):
            country_to_co2[keys[i]] = 0 
            
        for i in range(len(keys)):
            #if there is already a co2 amount assigned to the country (ie >0 value), then 
            # add on the new value to avoid replacing the value:

            if country_to_co2[keys[i]] >0:
                country_to_co2[keys[i]] = country_to_co2[keys[i]] + values[i]        
            else:
                country_to_co2[keys[i]] =  values[i]
                
                
        return country_to_co2




    def summary(self, city: City):
        co2_tonnes_rounded = int(round(  self.total_co2(city)/1000  ))
        
        print("Host city: {} ({})".format(city.city, city.country) )
        print("Total CO2: {} tonnes".format(   co2_tonnes_rounded    ))
        print("Total attendees travelling to {} from {} different cities: {}".format(city.city, len(self.cities), self.total_attendees()))


    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        sorted_city_co2 = []
        city_names = [i.city for i in self.cities]
        co2_emissions  = [self.total_co2(i) for i in self.cities]
        

        #create 2 "columns"; city names and the emmisions if they were the host city:
        for i in self.cities:
            sorted_city_co2.append( (  i.city, self.total_co2(i)  ) )  
        
        
        sorted_city_co2.sort( key=lambda x: x[1]) #sort by second column (ie ammount of co2)
        return sorted_city_co2


    def plot_top_emitters(self, city: City, n: int, save: bool):
        raise NotImplementedError






#checking that functions are working correctly:

manny = City('manchester', 'UK', 21, 39.22, 30.33) # made up values
ny = City('NY', 'USA', 21, 38.22, 28.33)
d = City('Dublin', 'Ireland', 52, 46.22, 2.33)
l = City('London', 'UK', 21, 45.22, 18.33)

cities_list = [d, l, ny, manny]



city_collection = CityCollection(cities_list)

print(city_collection.total_distance_travel_to(ny))



z = City('Zurich', 'Switzerland', 52, 47.22, 8.33)
city_collection.summary(z)

