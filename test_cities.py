import pytest
from pytest import raises, approx
from cities import *
from utils import *

#extracted from csv file:
algiers = City('Algiers', 'Algeria', 1, 28.0000272, 2.9999825)
pergamino = City('Pergamino', 'Argentina', 1, -33.8951226, -60.5663735)
sydney = City('Sydney', 'Australia', 41, -33.8548157, 151.2164539)
richmond = City('Richmond', 'Australia', 41, -33.6009721,150.7496405)
dhaka = City('Dhaka', 'Bangladesh', 10, 23.7593572, 90.3788136)

city_list = [pergamino, sydney, richmond,  dhaka]
collection = CityCollection(city_list)
#print(algiers.distance_to(pergamino))
#print(algiers.co2_to(pergamino))
#print(collection.total_co2(algiers))
#print(collection.countries())
#print(collection.total_attendees())
brisbane = City('Brisbane', 'Australia', 6, -27.4689682, 153.0234991) 
perth = City('Perth', 'Australia', 17, -31.9527121, 115.8604796) 

print(richmond.distance_to(sydney))
print(sydney.distance_to(perth))

#print(collection.co2_by_country(algiers))

#for i in city_list:
    #print(collection.total_co2(i))

#print(collection.sorted_by_emissions()[0])

def test_distance_to():
    result = algiers.distance_to(pergamino)
    expected = 9596.676 #calculated using excel

    assert approx(expected, rel = 0.001)  == expected



def test_co2_to():
    result = algiers.co2_to(pergamino)
    expected = 2879002.712

    assert approx(expected, rel = 0.001)  == expected



def test_countries(): 
    result = collection.countries()
    expected = ['Argentina', 'Australia', 'Bangladesh'] #sort in alphabetical order

    assert result == expected



def test_total_attendees():
    result = collection.total_attendees()
    expected = 93

    assert result == expected
    


def test_total_distance_travel_to():
    result = collection.total_distance_travel_to(algiers)
    expected = 1481471.539

    assert approx(result, rel=0.001) == expected


def test_total_co2():
    result = collection.total_co2(algiers)
    expected = 444441461.582

    assert approx(result, rel = 0.001)   == expected




def test_travel_by_country():
    result = collection.travel_by_country(algiers)
    expected = {'Argentina': 9596.676, 'Australia': 1386330.243, 'Bangladesh': 85544.619}


    assert approx(result, rel = 0.001) == expected




def test_co2_by_country():
    result = collection.co2_by_country(algiers)
    expected = {'Argentina': 2879002.712, 'Australia': 415899072.947, 'Bangladesh': 25663385.922}


    assert approx(result, rel = 0.001) == expected




def test_co2_edge_case():
    '''Testing the limits/edge cases/if statements in co2_to() function
    '''
    perth = City('Perth', 'Australia', 17, -31.9527121, 115.8604796) #a city between 1000-8000 km of sydney


    #for <1000km if statement:
    result1 = richmond.co2_to(sydney)/(  richmond.distance_to(sydney)*richmond.attendee_num  ) #only want scalefactor
    expected1 = 200

    #1000-8000km:
    result2 = sydney.co2_to(perth)/(  sydney.distance_to(perth)*sydney.attendee_num  )
    expected2 = 250

    #>8000km:
    result3 = sydney.co2_to(algiers)/(  sydney.distance_to(algiers)*sydney.attendee_num  )
    expected3 = 300


    assert approx(result1) == expected1
    assert approx(result2) == expected2
    assert approx(result3) == expected3





def test_sorted_by_emissions():
    result = collection.sorted_by_emissions()
    expected = [('Richmond', 31040794.376), ('Sydney', 31181900.729), ('Dhaka', 227694996.767) , ('Pergamino', 341389884.731)  ] #sorted by emmision (low to high)

    assert [tuples[0] for tuples in result] == [tuples[0] for tuples in expected] #names
    assert approx([tuples[1] for tuples in result], rel=0.001) == [tuples[1] for tuples in expected] #emmision values

    



####################### NEGATIVE TESTS #########################

def test_negative_City_inputs():
    with pytest.raises(TypeError):
        wrong_city_type = City(0, 'Test', 2, -18, -18)
    with pytest.raises(TypeError):
        wrong_country_type = City('Test', 0, 2, -18, -18)


    with pytest.raises(ValueError):
        negative_attendees = City('Test', 'Test', -2, -18, -18)
    with pytest.raises(TypeError):
        wrong_attendees_type = City('Test', 'Test', 2.1, -18, -18)




    with pytest.raises(ValueError):
        lat_out_of_range = City('Test', 'Test', 2, 300, -18)
    with pytest.raises(ValueError):
        lat_out_of_range = City('Test', 'Test', 2, -300, -18)

    with pytest.raises(ValueError):
        long_out_of_range = City('Test', 'Test', 2, 300, -18)
    with pytest.raises(ValueError):
        long_out_of_range = City('Test', 'Test', 2, -300, -18)



    with pytest.raises(TypeError):
        wrong_lat_type = City('Test', 'Test', 2, 'Test', -18)
    with pytest.raises(TypeError):
        wrong_long_type = City('Test', 'Test', 2, -18, 'Test')





def test_negative_n_value():
    with pytest.raises(ValueError):
        n_larger_than_countries = collection.plot_top_emitters(algiers, 1000, False)
    with pytest.raises(TypeError):
        wrong_n_type = collection.plot_top_emitters(algiers, 'Test', False)


def test_negative_save_type():
    with pytest.raises(TypeError):
        wrong_save_type = collection.plot_top_emitters(algiers, 3, 'Test')


def test_negative_collection_list():
    with pytest.raises(ValueError):
        empty_list = CityCollection([])

    with pytest.raises(TypeError):
        not_list_type = CityCollection({'Test', 'Test'})



def test_negative_City_objects():
    with pytest.raises(TypeError):
        incorrect_host_city_type = algiers.distance_to('pergamino')
    with pytest.raises(TypeError):
        incorrect_host_city_type = algiers.co2_to('pergamino')


    with pytest.raises(TypeError):
        CityCollection([algiers, 'algiers', dhaka])
    with pytest.raises(TypeError):
        incorrect_host_city_type = collection.total_distance_travel_to('algiers')
    with pytest.raises(TypeError):
        incorrect_host_city_type = collection.travel_by_country('algiers')
    with pytest.raises(TypeError):
        incorrect_host_city_type = collection.total_co2('algiers')
    with pytest.raises(TypeError):
        incorrect_host_city_type = collection.co2_by_country('algiers')
    with pytest.raises(TypeError):
        incorrect_host_city_type = collection.summary('algiers')
    with pytest.raises(TypeError):
        incorrect_host_city_type = collection.sorted_by_emissions('algiers')
    with pytest.raises(TypeError):
        incorrect_host_city_type = collection.plot_top_emitters('algiers')
                

