import json
import csv

# Kinda hacky - if the map doesn't find a match in the source json, uses the mapped field name instead
METADATA_MAP = {
    "ItemType":"Person", 
    "Dublin Core:Title":"Name",
    "Dublin Core:Subject":"Category",
    "Dublin Core:Description":"Biographical entry imported from The HistoryMakers",
    "Dublin Core:Creator":'<a href="https://www.thehistorymakers.org/">The HistoryMakers</a>',
    "Dublin Core:Source":"", # placeholder for header
    "Dublin Core:Publisher":"The HistoryMakers",
    "Dublin Core:Rights":"©2020 The HistoryMakers. All rights reserved.",
    
    "Item Type Metadata:Birthplace":"Birth Location",
    "Item Type Metadata:Birth Date":"Born",
    "Item Type Metadata:Occupation":"Occupation(s)"
}


def strip_ws(s):
    return ', '.join(ss.strip() for ss in s.split('\n'))

def map_metadata(person, json):
    for field in METADATA_MAP:
        if METADATA_MAP[field] in json:
            person[field] = strip_ws(json[METADATA_MAP[field]])
        else:
            person[field] = METADATA_MAP[field]

persons = []
with open("PoliticalBios.json","r") as biosjson:
    bios = json.load(biosjson)
    for url in bios:
        person = {}
        map_metadata(person,bios[url])
        ## fill in special fields
        person["Dublin Core:Source"] = url
        person["Dublin Core:Description"] = '<a class="about__link" href="'+url+'">To see the entire interview, click here</a>'
        persons.append(person)

with open('PoliticalMakers.csv', 'w', newline='') as csvfile:
    fieldnames = METADATA_MAP.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for person in persons:
        writer.writerow(person)