from Database import Database
from Piloto import Piloto
from Passageiro import Passageiro
from Voo import Voo
from pymongo import MongoClient
from bson.objectid import ObjectId

class PilotoDAO:

    def __init__(self):
        self.db = Database("ProjetoFinal", "Pilotos")
    
    def createPiloto(self, piloto: Piloto):
        pilotoJSON = self.__pilotoToJSON(piloto)
        try:
            res = self.db.collection.insert_one(pilotoJSON)
            print(f"Piloto criado com sucesso com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o piloto: {e}")
            return None

    def readPilotoById(self, id: str) -> Piloto:
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Piloto encontrado:")
            return self.__criaPiloto(res)
        except Exception as e:
            print(f"Ocorreu um erro ao buscar buscar o piloto: {e}")
            return None
        
    def readAllPilotos(self):
        try:
            res = self.db.collection.find()
            return [self.__criaPiloto(piloto) for piloto in res]
        except Exception as e:
            print(f"Ocorreu um erro ao buscar buscar os pilotos: {e}")
            return None

    def updatePiloto(self, id: str, piloto: Piloto):
        pilotoJSON = self.__pilotoToJSON(piloto)
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": pilotoJSON})
            print(f"Piloto atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o piloto: {e}")
            return None

    def deletePiloto(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Piloto excluído: {res.deleted_count} documento(s) excluído(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o piloto: {e}")
            return None
    
    def __pilotoToJSON(self, piloto: Piloto):
        voos = [self.__getDadosVoo(voo) for voo in piloto.voos]
        return {"nome": piloto.nome, "telefone": piloto.telefone, "cpf": piloto.cpf, "numVoos": piloto.numVoos, "voos": voos}
    
    def __getDadosVoo(self, voo: Voo):
        dadosPassageiro = {"nome": voo.passageiro.nome, "telefone": voo.passageiro.telefone, "cpf": voo.passageiro.cpf}
        return {"data": voo.data, "duracao": voo.duracao, "altMax": voo.altMax, "numFotos": voo.numFotos, "equipamento": voo.equipamento, "passageiro": dadosPassageiro}
    
    def __criaPiloto(self, pilotoJSON):
        voos = [self.__criaVoo(voo) for voo in pilotoJSON["voos"]]
        return Piloto(pilotoJSON["nome"], pilotoJSON["telefone"], pilotoJSON["cpf"], voos)
    
    def __criaVoo(self, vooJSON):
        passageiro = Passageiro(vooJSON["passageiro"]["nome"], vooJSON["passageiro"]["telefone"], vooJSON["passageiro"]["cpf"])
        return Voo(vooJSON["data"], vooJSON["duracao"], vooJSON["altMax"], vooJSON["numFotos"], vooJSON["equipamento"], passageiro)
    
    