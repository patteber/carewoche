import json

class Carewoche:
    def __init__(self, file) -> None:
        self.file = file
        with open(file, mode='r') as f:
            self.data = json.load(f)
            
    def writeFile(self, suffix = ""):
        json_object = json.dumps(self.getData(), indent=4)
        with open(self.file + suffix, "w") as outfile:
            outfile.write(json_object)

    def getData(self):
        return self.data

    def getMembers(self):
        return self.data["Members"]
    
    def postMember(self, name, active):
        m = self.getMembers()
        o = self.getOrder()
        isNew = False if name in m else True
        if isNew: # create
            m[name] = {"IsActive": active}
            if active: 
                o.append(name)
        else: # update
            if active:
                self.activateMeber(name)
            else:
                self.deactivateMeber(name)
    
    def deleteMember(self, name):
        m = self.getMembers().pop(name, None)
        if m != None and m["IsActive"]:
            o = self.getOrder()
            o.pop(o.index(name))
    
    def getOrder(self):
        return self.data["Order"]
        
    def activateMeber(self, name):
        self.getMembers()[name]["IsActive"] = True
        if not name in self.getOrder():
            self.getOrder().append(name)
    
    def deactivateMeber(self, name):
        self.getMembers()[name]["IsActive"] = False
        o = self.getOrder()
        o.pop(o.index(name))
    
    def iterateOrder(self):
        o = currOrder = self.getOrder()
        o.insert(len(o)-1, o.pop(0))
        
    def changeMembersOrder(self, name, offset):
        o = self.getOrder()
        currIdx = o.index(name)
        newIdx = (currIdx + offset) % len(o)
        if newIdx < 0:
            newIdx += len(o) - 1
        o.insert(newIdx, o.pop(currIdx))
        