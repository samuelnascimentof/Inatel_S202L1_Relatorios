from database import Database

class ProductAnalyzer:

    db = None

    def __init__(self):
        self.db = Database(database="mercado", collection="compras")
        # self.db.resetDatabase()

    # Retorna o total de vendas no dia
    def totalVendasNoDia(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1}},
        ])
        return result

    # Retorna o produto mais vendido em todas as compras
    def produtoMaisVendido(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        return result

    # Retorna o cliente que mais gastou em uma única compra
    def clienteQueMaisGastou(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        return result

    # Retorna todos os produtos que tiveram uma quantidade vendida acima de 1 unidade
    def produtosVendidosAcimaDeUmaUnidade(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            # {"$sort": {"total": {"$gt": "1"}}}
        ])
        return result