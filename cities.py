from typing import Dict, List, Tuple
from math import asin, sin, cos, sqrt, radians
import matplotlib.pyplot as plt

class City:
    def __init__(self, city, country, attendee_num, latitude, longitude):
        self.city = city
        self.country = country
        self.attendee_num = attendee_num #number of attendees
        self.latitude = latitude
        self.longitude = longitude



        #create errors to  check for valid values and types of inputs:
        if type(city) != str or type(country) != str:
            raise TypeError("City name and country name must be a string.")

        if attendee_num < 0:
            raise ValueError("Number of attendees is negative.") 
        if type(attendee_num) != int:
            raise TypeError("Number of attendees must be an integer.")


        if latitude > 90 or latitude < -90:
            raise ValueError("Latitude is invald; must be between (-90, 90).") 
        if longitude >180 or longitude <-180:
            raise ValueError("Longitude is invald; must be between (-180, 180).") 


        if type(longitude) != float and type(longitude) != int:
            raise TypeError("Longitude must be a float or integer.") 
        if type(latitude) != float and type(latitude) != int:
            raise TypeError("Latitude must be a float or integer.") 





    
    def distance_to(self, other: 'City') -> float:
        '''use Haversine formula to calculate distance between 2 cities'''

        #check input is a `City` object (inlcluded in all City object-dependent functions):
        if type(other) != City:
            raise TypeError("Input `other` must be a `City` object.")


        R=6371 #radius of earth
        first_term = sin(radians(   other.latitude/2  -  self.latitude/2   ))**2 #first term in equation
        second_term = cos(radians(   self.latitude   ))*cos(radians(  other.latitude  ))*( sin(radians(  other.longitude/2 - self.longitude/2  ))**2 ) #second term in equation

        d = 2*R*asin(sqrt(  first_term + second_term   )) #distance 

        return d
    


    def co2_to(self, other: 'City') -> float:
        '''co2 released to travel from one city (`self`) to host city (`other`) by all attendees'''
        #if type(other) != City:
            #raise TypeError("Input `other` must be a `City` object.")



        distance_between_cities = self.distance_to(other)


        if distance_between_cities <= 1000: #public transport
            return 200*distance_between_cities*self.attendee_num

        if 1000< distance_between_cities <=8000: #short-haul flight
            return 250*distance_between_cities*self.attendee_num

        if distance_between_cities > 8000: #long-haul flight
            return 300*distance_between_cities*self.attendee_num           

 
class CityCollection:
    def __init__(self, cities):
        self.cities = cities
        
        if type(cities) != list: #input must be a list
            raise TypeError("Input must be a list of `City` objects.")
        if len(cities) == 0: #list must not be empty
            raise ValueError("Input list is empty.")

        for i in cities: #test that each item in list is a `City` object
            if type(i) != City:
                raise TypeError("Input list items must all be `City` objects.")



    def countries(self) -> List[str]:
        '''A list of unique country names'''
        countries = set([i.country for i in self.cities])#a set only extracts unique values (countries in this case)
        
        return sorted( list(countries),  key=str.lower) #make list and sort in alphabetical order



    def total_attendees(self) -> int:
        '''The number of attendees in all cities'''
        return sum( [i.attendee_num for i in self.cities] )
        


    def total_distance_travel_to(self, city: City) -> float:
        '''The total distance travelled by attendees from all cities (excluding the host city) to the host city'''
        if type(city) != City:
            raise TypeError("Input host city must be a `City` object.")


        total_distance = sum( [i.distance_to(city)*i.attendee_num for i in self.cities] )

        return total_distance




    def travel_by_country(self, city: City) -> Dict[str, float]:
        '''A dictionary of a mapping of countries to the distance travelled by all attendees from that country to the host city'''
        if type(city) != City:
            raise TypeError("Input host city must be a `City` object.")


        country_to_distance = {}
        keys = [str(i.country) for i in self.cities]
        values = [i.distance_to(city)*i.attendee_num for i in self.cities]


        #assign 0 to each key:        
        for i in range(len(keys)):
            country_to_distance[keys[i]] = 0 

        
        for i in range(len(keys)):   
            #if there is already a distance assigned to the country (ie >0 value), then
            #add on the new value to avoid replacing the value:

            if country_to_distance[keys[i]] >0:
                country_to_distance[keys[i]] = country_to_distance[keys[i]] + values[i]        
            else:
                country_to_distance[keys[i]] =  values[i]
                
            
       
        return country_to_distance





    def total_co2(self, city: City) -> float:
        '''The total co2 released by attendees from all cities (excluding the host city) to the host city'''
        if type(city) != City:
            raise TypeError("Input host city must be a `City` object.")

        total_co2 = sum( [i.co2_to(city) for i in self.cities] )
        return total_co2




    def co2_by_country(self, city: City) -> Dict[str, float]:
        '''A dictionary of a mapping of countries to the co2 released by all attendees from that country to the host city'''
        if type(city) != City:
            raise TypeError("Input host city must be a `City` object.")


        country_to_co2 = {}
        keys = [str(i.country) for i in self.cities]
        values = [i.co2_to(city)for i in self.cities]
        

        
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
        '''Printed summary of important info: 
        Host city and it's country, 
        Total CO2 released to get to that city by all attendees, 
        Total attendees travelling'''
        if type(city) != City:
            raise TypeError("Input host city must be a `City` object.")


        co2_tonnes_rounded = int(round(  self.total_co2(city)/1000  ))
        
        print("Host city: {} ({})".format(city.city, city.country) )
        print("Total CO2: {} tonnes".format(   co2_tonnes_rounded    ))
        #print("Total attendees travelling to {} from {} different cities: {}".format(city.city, len(self.cities)-1, self.total_attendees()-city.attendee_num))
        if city in self.cities:
            print("Total attendees travelling to {} from {} different cities: {}".format(city.city, len(self.cities)-1, self.total_attendees()-city.attendee_num))

        else:
            print("Total attendees travelling to {} from {} different cities: {}".format(city.city, len(self.cities), self.total_attendees()))

        




    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        '''A list of cities and the emmisions if that city was the host '''
        sorted_city_co2 = []
        
        #create 2 "columns"; city names and the emmisions if they were the host city:
        for i in self.cities:
            sorted_city_co2.append( (  i.city, self.total_co2(i)  ) )  
        
        
        sorted_city_co2.sort( key=lambda x: x[1]) #sort by second column (ie ammount of co2)
        return sorted_city_co2








    def plot_top_emitters(self, city: City, n: int=10, save: bool=False):
        '''A bar chart of the top n countries with the most emmisions by the attendees when travelling to the host city. 
        The other countries are added and displayed as an individual bar.'''
        if type(city) != City:
            raise TypeError("Input host city must be a `City` object.")



        #test for datatype and value of n:
        if n> len(self.countries()):
            raise ValueError("`n` must be less than or equal to the number of countries in collection.")
        if type(n) != int:
            raise TypeError("`n` must be an integer.") 

        #test for datatype of save:
        if type(save) != bool:
            raise TypeError("`save` must be a boolean.")
        

        sorted_country_co2 = []


        #convert co2 by country dictionary into two-column list:
        countries = list(self.co2_by_country(city).keys())
        co2 = list(self.co2_by_country(city).values())
        
        for i in range(len(countries)):
            sorted_country_co2.append( [  countries[i], co2[i]/1000  ] ) #co2/1000 to convert to tonnes
            
            
        sorted_country_co2.sort( key=lambda x: x[1], reverse=True) #sort from highest co2 to lowest     



        #extract names and co2 values from 2-column list:    
        country_names = [sorted_country_co2[i][0] for i in range(len(countries))]
        co2_values = [sorted_country_co2[i][1] for i in range(len(countries))]
        
        
     
        
        x_countries = country_names[0:n] #range from 0:n
        y_co2 = co2_values[0:n]
        
        other_countries = 'Everywhere else'
        other_co2 = sum(  co2_values[n:]  ) #sum residual/remaining co2 values
        
        #add 'everywhere else' countries and values onto lists
        x_countries = x_countries + [other_countries] 
        y_co2 = y_co2 + [other_co2]
        
        x_countries_pos = [i for i, _ in enumerate(x_countries)] #assign positions to country strings
        



        plt.figure()
        plt.bar(x_countries_pos, y_co2)
        plt.xticks(x_countries_pos, x_countries, rotation=35)
        plt.title('Total Emissions From Each Country (Top {})'.format(n))
        plt.ylabel('Total CO2 Emissions (Tonnes)')
        plt.tight_layout()
        
        if save == True:
            form = ('_'.join(city.city.split())).lower() #include underscore and host city in filename
            plt.savefig('{}.png'.format(form))

        plt.show()
        