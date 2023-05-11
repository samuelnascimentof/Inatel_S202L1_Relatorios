class PlayerMatchDatabase:
    def __init__(self, database):
        self.db = database
    

    
    def create_player(self, name, playerId):
        query = "CREATE (:Player {name: $name, playerId: $playerId})"
        parameters = {"name": name, "playerId": playerId}
        self.db.execute_query(query, parameters)
    
    def create_match(self, matchId, players, winner):
        # Creates the match node
        query = "CREATE (:Match {matchId: $matchId, players: $players, winner: $winner})"
        parameters = {"matchId": matchId, "players": players, "winner": winner}
        self.db.execute_query(query, parameters)

        # Creates the relationship between the match and the players
        for player in players:
            if player == winner:
                query = "MATCH (p:Player {name: $player}) MATCH (m:Match {matchId: $matchId}) CREATE (p)-[:PLAYED]->(m) CREATE (p)-[:WON]->(m)"
                parameters = {"player": player, "matchId": matchId}
                self.db.execute_query(query, parameters)

            else:
                query = "MATCH (p:Player {name: $player}) MATCH (m:Match {matchId: $matchId}) CREATE (p)-[:PLAYED]->(m)"
                parameters = {"player": player, "matchId": matchId}
                self.db.execute_query(query, parameters)



    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name, p.playerId AS playerId"
        results = self.db.execute_query(query)
        return [(result["name"], result["playerId"]) for result in results]
    
    def get_matches(self):
        query = "MATCH (m:Match) RETURN m.matchId AS matchId, m.players AS players, m.winner AS winner"
        results = self.db.execute_query(query)
        return [(result["matchId"], result["players"], result["winner"]) for result in results]
    
    def get_match(self, matchId):
        query = "MATCH (p:Match {matchId: $matchId}) RETURN p.matchId AS matchId, p.players AS players, p.winner AS winner"
        parameters = {"matchId": matchId}
        results = self.db.execute_query(query, parameters)
        return [(result["matchId"], result["players"], result["winner"]) for result in results]
    
    def get_player_matches(self, name):
        query = "MATCH (p:Player {name: $name})-[:PLAYED]-(m:Match) RETURN m.matchId AS matchId, m.players AS players, m.winner AS winner"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [(result["matchId"], result["players"], result["winner"]) for result in results]
    


    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
    
    def update_matchId(self, old_matchId, new_matchId):
        query = "MATCH (p:Match {matchId: $old_matchId}) SET p.matchId = $new_matchId"
        parameters = {"old_matchId": old_matchId, "new_matchId": new_matchId}
        self.db.execute_query(query, parameters)
    
    def update_matchPlayers(self, matchId, players):
        query = "MATCH (p:Match {matchId: $matchId}) SET p.players = $players"
        parameters = {"matchId": matchId, "players": players}
        self.db.execute_query(query, parameters)
    
    def update_matchWinner(self, matchId, winner):
        query = "MATCH (p:Match {matchId: $matchId}) SET p.winner = $winner"
        parameters = {"matchId": matchId, "winner": winner}
        self.db.execute_query(query, parameters)



    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_match(self, matchId):
        query = "MATCH (p:Match {matchId: $matchId}) DETACH DELETE p"
        parameters = {"matchId": matchId}
        self.db.execute_query(query, parameters)
    