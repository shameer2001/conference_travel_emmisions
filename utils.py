from cities import City, CityCollection
from pathlib import Path
import csv

file_path = Path("attendee_locations.csv")

def read_attendees_file(filepath: Path) -> CityCollection:
    with open(filepath) as file:
        csv_reader = csv.reader(file, delimiter=',')

        next(csv_reader) #skip header

        #attendee_nums = [int(row[0]) for row in csv_reader]
        #countries = [str(row[1]) for row in csv_reader]
        #US_states =  [str(row[2]) for row in csv_reader]
        #cities =  [str(row[3]) for row in csv_reader]
        #latitudes =  [float(row[4]) for row in csv_reader]
        #longitudes =  [float(row[5]) for row in csv_reader]

        attendee_nums =[]
        countries=[]
        US_states=[]
        cities=[]
        latitudes=[]
        longitudes=[]


        for row in csv_reader:
            attendee_nums.append( int(row[0]) )
            countries.append( str(row[1]) )
            US_states.append( str(row[2]) )
            cities.append( str(row[3]) )
            latitudes.append( float(row[4]) )
            longitudes.append( float(row[5]) )


        all_City_objects = [City(cities[i], countries[i], attendee_nums[i], latitudes[i], longitudes[i]) for i in range(len(cities))]

        all_City_objects_dict = {}
         
        for i in range(len(cities)):
            all_City_objects_dict[cities[i]] = all_City_objects[i]

        #print(attendee_nums)
        #print(countries)

        #for i in range(len(cities)):
            #exec("%s = %d" % (cities[i], all_City_objects[i]))

        return CityCollection(all_City_objects), all_City_objects_dict


collection = read_attendees_file(file_path)[0]
city_dict = read_attendees_file(file_path)[1]
#print(read_attendees_file(file_path)[2])

#collection.plot_top_emitters(city_dict['San Francisco'], 7, False)


#collection.plot_top_emitters(city_dict['San Francisco'], 7, False) 

print(city_dict['Zurich'].distance_to(city_dict['San Francisco']))

zurich = City('Zurich', 'Switzerland', 52, 47.22, 8.33)
san_francisco = City('San Francisco', 'United States', 71, 37.77, -122.41)

print(zurich.co2_to(san_francisco))


#print(collection.total_distance_travel_to(zurich))
#print(sum(collection.travel_by_country(zurich).values()))
#print(collection.travel_by_country(zurich))
#print(collection.total_co2(zurich))
#print(collection.co2_by_country(zurich))

#print(collection.sorted_by_emissions())
collection.plot_top_emitters(zurich, 7, False) 
collection.summary(zurich)

