import en_core_web_sm
import urllib.request
from tqdm import tqdm
import pandas as pd

from geopy.geocoders import Nominatim


nlp = en_core_web_sm.load()

def getDataFromURL(url): 
    return urllib.request.urlopen(url).read()

def getLocationData():
    url = 'https://www.gutenberg.org/files/103/103-0.txt'
    locations = []
    data = getDataFromURL(url)
    doc = nlp(str(data))
    [locations.append(loc.text) for loc in doc.ents if loc.label_ == 'LOC']
    return locations

def getLatitudeAndLongitudeFromCityName(city_list):
    locations = []
    geolocator = Nominatim(user_agent="TestApp")
    for city in tqdm(city_list):
        try:
            location = geolocator.geocode(city)
            locations.append((city,location.latitude, location
    .longitude))
        except Exception as e:
            locations.append((city, 0, 0)) 
    return locations

def main(): 
    locations = getLocationData()
    latAndlong = getLatitudeAndLongitudeFromCityName(locations)
    df = pd.DataFrame(latAndlong, columns=['Place','Lat','Long'])
    df.to_csv("dataset.csv")

def saveDataset():
    url = 'https://www.gutenberg.org/files/103/103-0.txt'
    data = getDataFromURL(url)
    with open("words.txt", "w") as f: 
        f.write(str(data))

if __name__ == "__main__":
    main()
    # saveDataset()
    