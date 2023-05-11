from database import Database
from player_match_database import PlayerMatchDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://18.206.123.219:7687", "neo4j", "barrel-crashes-inception")
db.drop_all()

playerMatch_db = PlayerMatchDatabase(db)

# Criando jogadores
playerMatch_db.create_player("João", 1)
playerMatch_db.create_player("Maria", 2)
playerMatch_db.create_player("José", 3)
playerMatch_db.create_player("Ana", 4)
playerMatch_db.create_player("Carlos", 5)

# Criando partidas
playerMatch_db.create_match(1001, ["João", "Maria", "José"], "João")
playerMatch_db.create_match(1002, ["Ana", "Carlos", "João"], "Ana")
playerMatch_db.create_match(1003, ["Maria", "José", "Ana"], "Maria")

# Atualizando o vencedor de uma partida
playerMatch_db.update_matchWinner(1001, "José")

# Atualizando os jogadores de uma partida
playerMatch_db.update_matchPlayers(1001, ["João", "Maria", "Ana"])

# Atualizando o Id de uma partida
playerMatch_db.update_matchId(1001, 1004)

# Atualizando o nome de um jogador
playerMatch_db.update_player("João", "Pedro")

# Deletando um jogador e uma partida
playerMatch_db.delete_player("Ana")
playerMatch_db.delete_match(1003)

# Imprimindo os jogadores cadastrados
print("Jogadores:")
print(playerMatch_db.get_players())

# Imprimindo as partidas cadastradas
print("Partidas:")
print(playerMatch_db.get_matches())

# Imprimindo as partidas de um jogador
print("Partidas da Maria:")
print(playerMatch_db.get_player_matches("Maria"))

# Imprimindo dados de uma partida
print("Dados da partida 1002:")
print(playerMatch_db.get_match(1002))

# Fechando a conexão com o banco de dados
db.close()