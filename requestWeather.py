
"""

Wrapper for darksky api

gets the weather data in json format

Usage :

weather = requestWeather([key],[lat],[long])
print(weather.GetWeatherData())

"""

import sys
import requests

__author__ = 'freezer9'

"""
# coords of New York
Latitude = 40.730610
Longitude = -73.935242

"""

darksky_api_url = "https://api.darksky.net/forecast/"
darksky_api_key = "[KEY]"

class requestWeather(object):

# format :https://api.darksky.net/forecast/[key]/[lat],[long]



    def __init__(self,api_key=None,Latitude=None,Longitude=None):

        if len(api_key) == 32:
            self.api_key = api_key
            if Latitude is not None and Longitude is not None:
                self.Latitude = Latitude
                self.Longitude = Longitude
            else:
                print('Latitude and Longitude are required')
        else:
            print('Not a valid API key!')

    def GetWeatherData(self):
        '''
        returns the weather data in json format
        '''
        return self.GetJsonData()


    def BuildUrl(self,lat,longi):
        '''
        Builds the url using the lat and long to request to the darksky api
        '''
        self.lat = lat
        self.longi = longi
        try:
            float(self.lat)
            float(self.longi)
        except ValueError:
            try:
                self.lat   += 0.0000
                self.longi += 0.0000
            except ValueError:
                print("Can't convert to float! ")

        # build the url
        self.url = darksky_api_url + self.api_key + '/'
        self.url += str(self.lat) + ',' + str(self.longi)
        return self.url



    def HttpGetRequest(self):
        '''
        connects to the darknet server to get the weather data and returns json data
        '''
        try:
            # try to send a request
            self.resq_data = requests.get(self.BuildUrl(self.Latitude,self.Longitude),timeout = 10.0)
            if self.resq_data.status_code != 200:
                print('Failed to send a request!')
                try:
                    # try to send a request again
                    print('Sending again...')
                    self.resq_data = requests.get("https://api.darksky.net/forecast/{0}/{1},{2}".format(self.api_key,self.Latitude,self.Longitude,timeout = 10.0))
                except requests.exceptions.RequestException as e:
                    print("Error:",e)
                except requests.exceptions.Timeout:
                    print("request timed out!")
                    sys.exit(1)
        # http exceptions                                                                     )
        except requests.exceptions.RequestException as e:
            print("Can't request for the data! :",e)
        except requests.exceptions.Timeout:
            print("request timed out!")
            sys.exit(1)
        except requests.exceptions.TooManyRedirects:
            print('Too many redirections!')
            sys.exit(1)

        # store the response as json data
        self.response_data = None
        try:
            import json
            self.response_data = json.loads(self.resq_data.text)
        except TypeError:
            try:
                self.response_data = self.resq_data.json()
            except TypeError:
                print("Can't get the json data")
        return self.response_data

    def GetJsonData(self):
        ''' returns the json data from HttpGetRequest() method'''
        return self.HttpGetRequest()


if __name__ == '__main__':

    La = 40.730610
    Lo = -73.935242
    key = '[KEY]'

    weather = requestWeather(key,La,Lo)
    print(weather.GetWeatherData())
