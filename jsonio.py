import json
#from json_checker import Checker

class jsonio:
    listeSchema = {
        "liste" : [str]
    }
    
    def __init__(self, file) -> None:
        with open(file, mode='r') as f:
            self.data = json.load(f)
            # validate(data, schema)
     
    # def validate(data, schema):
    #      check = Checker(schema, soft=True)
    #      check.validate(data)

    def getData(self):
        return self.data

    def getMembers(self):
        return self.data["Members"]
    
    def getOrder(self):
        return self.data["Order"]
    
    def setOrder(self, newOrder) -> None:
        self.data["Order"] = newOrder
    
    def iterateOrder(self):
        currOrder = self.getOrder()
        length = len(currOrder)
        if length < 2:
            return 
        newOrder = [0]*length
        newOrder[length-1] = currOrder[0]
        i = 1
        while i < len(currOrder):
            newOrder[i-1] = currOrder[i]
            i += 1
        self.setOrder(newOrder)
        