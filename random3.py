import random

# Lista com as suas opções de decisão
respostas = ["Sim", "Não", "Com certeza não", "Esquece isso aí meu", "Vai dá não"]
sortenumber= [1,2,4,5,6,7,8]

# O programa escolhe uma resposta aleatoriamente
decisao = random.choice(respostas)

print(f"Decisão do destino: {decisao}")
