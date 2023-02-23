import requests
import json

key = '58bc8d83-7f76-4db9-829c-bb9861d08a69'
city = 'depok'
state = 'west java'
country = 'indonesia'

# url of Digital Forecast
url = 'http://api.airvisual.com/v2/city?city=' + city + '&state=' + state + '&country=' + country + '&key=58bc8d83-7f76-4db9-829c-bb9861d08a69'

# creating HTTP response object from given url
resp = requests.get(url)
data = json.loads(resp.content)

print(data['data']['city'])