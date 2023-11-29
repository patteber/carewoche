import json
#from json_checker import Checker

listeSchema = {
    "liste" : [str]
}

# def validate(data, schema):
#     check = Checker(schema, soft=True)
#     check.validate(data)

def getData(file, schema):
    with open(file, mode='r') as f:
        data = json.load(f)
        # validate(data, schema)
        return data
