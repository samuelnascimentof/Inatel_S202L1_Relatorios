from database import Database

class Pokedex:

    db: Database

    def __init__(self, database: Database):
        self.db = database

    def getByName(self, nome):
        return self.db.collection.find_one({"name": nome})
    
    def getByType(self, types: list):
        return self.db.collection.find({"type": {"$in": types}})
    
    def getByWeaknesses(self, weaknesses: list):
        return self.db.collection.find({"weaknesses": {"$in": weaknesses}})
    
    def getByTypeAndWeaknesses(self, types: list, weaknesses: list):
        return self.db.collection.find({"type": {"$in": types}, "weaknesses": {"$in": weaknesses}})
    
    def getAll(self):
        return self.db.collection.find()
    