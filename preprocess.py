import spacy
from geopy.geocoders import Nominatim
from tqdm import tqdm
import pandas as pd
import math

def preprocess(filename="words.txt"):
    with open(filename, "r") as f: 
        corpse = f.read()

    nlp = spacy.load("en_core_web_lg")

    with open("words.txt", "r") as f: 
        corpse = f.read()

    doc_corpse = nlp(corpse)

    location_data = set()
    new_loc_data = list()

    for ent in doc_corpse.ents:
        if ent.label_ == 'GPE' or ent.label_ == 'LOC':
            location_data.add(str(ent.text))
    for data in list(location_data): 
        new_loc_data.append(data.replace("\n", " "))
    
    del location_data
    
    return new_loc_data


def getLatAndLong(data):
    locs = []
    err_count = {
        "count": 0,
        "places": []
    }
    geolocator = Nominatim(user_agent="aroundTheWorldIn80Days")
    for place in tqdm(data): 
        try:
            loc = geolocator.geocode(place)
            locs.append((place, loc.latitude, loc.longitude))
        except Exception as e: 
            err_count["count"] += 1
            err_count["places"].append(place)
    return locs, err_count

def sortedDataFrame(df):
    df['sort_lat'] = df["Lat"].astype("float64")
    df['sort_long'] = df["Long"].astype("float64")

    df.sort_values(['sort_lat', 'sort_long'], ascending=True, inplace=True)
    df.drop(['sort_lat', 'sort_long'], axis='columns', inplace=True)
    return df

def saveDataFrame(df, filename="df.csv"): 
    df.to_csv(filename, index=False)

data = preprocess()
locs, err_count = getLatAndLong(data)

for loc in locs: 
    print(loc)
print(err_count)

dataframe = pd.DataFrame(locs, columns=["Place", "Lat", "Long"])
errorDataframe = pd.DataFrame(err_count["places"], columns=["Error_Places"])
dataframe = sortedDataFrame(dataframe)

saveDataFrame(df=dataframe)
saveDataFrame(df=errorDataframe, filename="error.csv")

