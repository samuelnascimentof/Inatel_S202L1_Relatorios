from database import Database

db = Database("bolt://54.174.170.232:7687", "neo4j", "picture-projectiles-world")

# Questão 1 - a)
query = "MATCH (t:Teacher{name:'Renzo'}) RETURN t.ano_nasc as ano, t.cpf as cpf"
results = db.execute_query(query)
print("Ano de nascimento e CPF do professor Renzo:")
for result in results:
    print(result['ano'], " - ", result['cpf'])

# Questão 1 - b)
query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name as name, t.cpf as cpf"
results = db.execute_query(query)
print("\nProfessores cujo nome começa com a letra M:")
for result in results:
    print(result['name'], " - ", result['cpf'])

# Questão 1 - c)
query = "MATCH (c:City) RETURN c.name as name"
results = db.execute_query(query)
print("\nCidades:")
for result in results:
    print(result['name'])

# Questão 1 - d)
query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name as name, s.address as address, s.number as number"
results = db.execute_query(query)
print("\nEscolas com numero entre 150 e 550:")
for result in results:
    print(result['name'], " - ", result['address'], " - ", result['number'])
    

# Questão 2 - a)
query = "MATCH (t:Teacher) RETURN MIN(t.ano_nasc) as velho, MAX(t.ano_nasc) as jovem"
results = db.execute_query(query)
for result in results:
    print("\nAno de nascimento do professor mais jovem: ",result['jovem'])
    print("Ano de nascimento do professor mais velho: ",result['velho'])

# Questão 2 - b)
query = "MATCH (c:City) RETURN AVG(c.population) as media"
results = db.execute_query(query)
for result in results:
    print("\nMédia de habitantes das cidades: ",result['media'])

# Questão 2 - c)
query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A') as name"
results = db.execute_query(query)
print("\nCidade com o cep 37540-000:")
for result in results:
    print(result['name'])

# Questão 2 - d)
query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 3, 1) as name"
results = db.execute_query(query)
print("\nCaractere iniciando a partir da terceira letra do nome:")
for result in results:
    print(result['name'])
