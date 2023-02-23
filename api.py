import requests
import xml.etree.ElementTree as ET

def bmkg(area,regency) :
    global daerah
    daerah = {}

    # url of Digital Forecast
    url = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-'+regency+'.xml'
  
    # creating HTTP response object from given url
    resp = requests.get(url)
  
    # saving the xml file
    with open('test.xml', 'wb') as f:
        f.write(resp.content)

    # Parse the xml file

    tree = ET.parse('test.xml')
    root = tree.getroot()

    path = './forecast/area/[@description=' + "'" + area + "'" +']'

    i = 0

    for movie in root.find(path):           

        if i >= 2:

            id = movie.get('id')
            daerah[id] = {}
            child_path = './forecast/area/[@description="Aceh Barat"]/parameter/[@id=' + '"' + id +  '"' + ']/timerange'

            for elem in root.findall(child_path):

                h =  elem.get('h')
                datetime = elem.get('datetime')

                if (h is None) or (len(h) == 0):
                    h = elem.get('day')
                    daerah[id].update({datetime: {'day': h, 'value': elem[0].text + ' ' +elem[0].get('unit')}})
                else:
                    daerah[id].update({datetime: {'hour': h, 'value': elem[0].text + ' ' + elem[0].get('unit')}})

        i += 1

    #print(daerah)
# bmkg("Aceh Barat","Aceh")

def iqair():
    print('Hell')