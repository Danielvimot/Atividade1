import random

# Lista com as suas opções de decisão
respostas = ["Sim", "Não", "Com certeza não", "Esquece isso aí meu"]

# O programa escolhe uma resposta aleatoriamente
decisao = random.choice(respostas)

print(f"Decisão do destino: {decisao}")
