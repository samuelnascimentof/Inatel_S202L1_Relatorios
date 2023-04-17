from Database import Database
from Motorista import Motorista
from Passageiro import Passageiro
from Corrida import Corrida
from pymongo import MongoClient
from bson.objectid import ObjectId

class MotoristaDAO:

    def __init__(self):
        self.db = Database("ExercicioAv1", "Motoristas")
    
    def createMotorista(self, motorista: Motorista):
        motoristaJSON = self.__motoristaToJSON(motorista)
        try:
            res = self.db.collection.insert_one(motoristaJSON)
            print(f"Motorista criado com sucesso com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None

    def readMotoristaById(self, id: str) -> Motorista:
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado: {res}")
            return self.__criaMotorista(res)
        except Exception as e:
            print(f"Ocorreu um erro ao buscar buscar o motorista: {e}")
            return None

    def updateMotorista(self, id: str, motorista: Motorista):
        motoristaJSON = self.__motoristaToJSON(motorista)
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": motoristaJSON})
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o motorista: {e}")
            return None

    def deleteMotorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista excluído: {res.deleted_count} documento(s) excluído(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o motorista: {e}")
            return None
    
    def __motoristaToJSON(self, motorista: Motorista):
        corridas = [self.__getDadosCorrida(corrida) for corrida in motorista.corridas]
        return {"nota": motorista.nota, "corridas": corridas}
    
    def __getDadosCorrida(self, corrida: Corrida):
        dadosPassageiro = {"nome": corrida.passageiro.nome, "documento": corrida.passageiro.documento}
        return {"nota": corrida.nota, "distancia": corrida.distancia, "valor": corrida.valor, "passageiro": dadosPassageiro}
    
    def __criaMotorista(self, motoristaJSON):
        corridas = [self.__criaCorrida(corrida) for corrida in motoristaJSON["corridas"]]
        return Motorista(motoristaJSON["nota"], corridas)
    
    def __criaCorrida(self, corridaJSON):
        passageiro = Passageiro(corridaJSON["passageiro"]["nome"], corridaJSON["passageiro"]["documento"])
        return Corrida(corridaJSON["nota"], corridaJSON["distancia"], corridaJSON["valor"], passageiro)
    
    