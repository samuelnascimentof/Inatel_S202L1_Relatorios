from database import Database
from Pokedex import Pokedex
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
pokedex = Pokedex(db)

pokemon = pokedex.getByName("Ivysaur")
pokemons = pokedex.getAll()
pokemons2 = pokedex.getByType(["Grass", "Poison"])
pokemons3 = pokedex.getByWeaknesses(["Fire", "Flying", "Ice", "Psychic"])
pokemons4 = pokedex.getByTypeAndWeaknesses(["Grass", "Poison"], ["Fire", "Flying", "Ice", "Psychic"])

writeAJson(pokemon, "pokemon")
writeAJson(pokemons, "pokemons")
writeAJson(pokemons2, "pokemons2")
writeAJson(pokemons3, "pokemons3")
writeAJson(pokemons4, "pokemons4")

