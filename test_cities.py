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
print(collection.total_co2(algiers))
print(collection.countries())
print(collection.total_attendees())


def test_distance_to():
    result = algiers.distance_to(pergamino)
    expected = 9596.676

    assert result == approx(expected, rel = 0.001)



def test_co2_to():
    result = algiers.co2_to(pergamino)
    expected = 2879002.712

    assert result == approx(expected, rel = 0.001)



# def test_countries(): ########
#     result = collection.countries()
#     expected = ['Australia',  'Argentina', 'Bangladesh']

#     assert result == expected



def test_total_attendees():
    result = collection.total_attendees()
    expected = 93

    assert result == expected
    


def test_total_distance_travel_to():
    result = collection.total_distance_travel_to(algiers)
    expected = 1481471.539

    assert result == approx(expected, rel = 0.001)


def test_total_co2():
    result = collection.total_co2(algiers)
    expected = 444441461.582

    assert result == approx(expected, rel = 0.001)    



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
