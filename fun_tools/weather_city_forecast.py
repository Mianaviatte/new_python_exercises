from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('ec597c946465133fbe795a355eb87b70')
mgr = owm.weather_manager()

city = input('What is your city? ')

observation = mgr.weather_at_place(city)
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75
w.visibility              # <bound method Weather.visibility of <pyowm.weatherapi25.weather.Weather - reference_time=2022-01-08 16:33:17+00:00, status=clouds, detailed_status=broken clouds>>


print('The weather in', city, 'is so nice, it\'s', w.humidity, '% humidity and', w.temperature('celsius').get('temp'), 'C in reality.')
print('It feels like', w.temperature('celsius').get('feels_like'), 'and', w.status)

reg = owm.city_id_registry()
list_of_locations = reg.locations_for(city)
city1 = list_of_locations[0]
lat = city1.lat  
lon = city1.lon  

one_call = mgr.one_call(lat, lon)
one_call.forecast_daily

print('Tommorrow morning it will be like', one_call.forecast_daily[0].status, "and like", one_call.forecast_daily[0].temperature('celsius').get('feels_like_morn', None), 'C.')
print('Next day morning it will be like', one_call.forecast_daily[1].status, "and like", one_call.forecast_daily[1].temperature('celsius').get('feels_like_morn', None), 'C.')
print('In two days morning it will be like', one_call.forecast_daily[2].status, "and like", one_call.forecast_daily[2].temperature('celsius').get('feels_like_morn', None), 'C.')
print('In tree day morning it will be like', one_call.forecast_daily[3].status, "and like", one_call.forecast_daily[3].temperature('celsius').get('feels_like_morn', None), 'C.')
print('In four day morning it will be like', one_call.forecast_daily[4].status, "and like", one_call.forecast_daily[4].temperature('celsius').get('feels_like_morn', None), 'C.')