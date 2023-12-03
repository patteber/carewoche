import json

class Carewoche:
    def __init__(self, file) -> None:
        with open(file, mode='r') as f:
            self.data = json.load(f)

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
        i = 0
        while i < length:
            newOrder[i] = currOrder[i+1 if i < length-1 else 0]
            i += 1
        self.setOrder(newOrder)
        
    def changeMembersOrder(self, id, offset):
        o = self.getOrder()
        currIdx = o.index(id)
        # to calculate zero-based index correctly using % 
        # we first add 1 calculate with % and substract 1 in the result
        newIdx = (currIdx + offset) % len(o)
        e = o.pop(currIdx)
        o.insert(newIdx, e)
        self.setOrder(o)
        