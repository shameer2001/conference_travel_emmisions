from cities import City, CityCollection
from pathlib import Path
import csv

file_path = Path("attendee_locations.csv")

def read_attendees_file(filepath: Path) -> CityCollection:
    '''Create a CityCollection object from a csv file containing properties of different cities'''

    with open(filepath) as file:
        csv_reader = csv.reader(file, delimiter=',')

        next(csv_reader) #skip header


        attendee_nums =[]
        countries=[]
        states=[]
        cities=[]
        latitudes=[]
        longitudes=[]


        for row in csv_reader:
            attendee_nums.append( int(row[0]) )
            countries.append( str(row[1]) )
            states.append( str(row[2]) )
            cities.append( str(row[3]) )
            latitudes.append( float(row[4]) )
            longitudes.append( float(row[5]) )

        #list of all city objects for all cities in csv file:
        all_City_objects = [City(cities[i], countries[i], attendee_nums[i], latitudes[i], longitudes[i]) for i in range(len(cities))] 

        return CityCollection(all_City_objects)


