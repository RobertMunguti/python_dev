import json

def readJsonFile(fileName):
    data=""  
    try:
        with open('Files/insulin.json') as json_file:
         data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data