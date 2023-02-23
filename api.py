import requests
import json

key = 'e89d4be9-162b-46e7-9c6d-47414f3a0a8f'

def iqair(country, state, city):

    global data

    # url of iqair API
    url = 'http://api.airvisual.com/v2/city?city=' + city + '&state=' + state + '&country=' + country + "&key=" + key 

    # HTTP respone and load the data
    resp = requests.get(url)
    data = json.loads(resp.content)


def nearest_city():

    global near

    url = "http://api.airvisual.com/v2/nearest_city?key=" + key 

    resp = requests.get(url)
    near = json.loads(resp.content)

    

