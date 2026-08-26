## A API original do desafio está fora do ar. Como solução, a DIO propôs simular o uso dela com uma lista

import pandas as pd
import random

dicas = [
    "{name}, comece investindo pouco e aumente aos poucos.",
    "{name}, tenha uma reserva de emergência antes de investir em ativos de maior risco.",
    "{name}, diversiique seus investimentos para reduzir riscos.",
    "{name}, deina seus objetivos antes de escolher onde investir.",
    "{name}, conheça seu peril de investidor.",
    "{name}, evite investir apenas porque alguém recomendou.",
    "{name}, estude o investimento antes de colocar seu dinheiro.",
    "{name}, não coloque todo o seu dinheiro em um único investimento.",
    "{name}, pense no longo prazo.",
    "{name}, tenha paciência e evite decisões por impulso.",
    "{name}, compare as taxas antes de investir.",
    "{name}, reinvista os rendimentos quando fizer sentido.",
    "{name}, acompanhe seus investimentos regularmente.",
    "{name}, não tente ganhar dinheiro rapidamente assumindo riscos excessivos.",
    "{name}, mantenha uma rotina de aportes, mesmo que sejam valores pequenos."
]


## EXTRACT
users = pd.read_csv('planilha.csv').to_dict(orient='records')


## TRANSFORM
def generate_tip(user):
    mensagem_base = random.choice(dicas)
    mensagem_final = mensagem_base.format(name=user['name'])
    return mensagem_final[:100]



for user in users:
    tip = generate_tip(user)
    print(f"Dica escolhida para {user['name']}:\n {tip} \n-----------")
    user['tip'] = tip


## LOAD
with open('LOAD.txt', 'w', encoding='utf-8') as file:
    file.write("Parte load\n")
    for user in users:
        id = user['id']
        nome = user['name']
        dica = user['tip']

        linha = f"ID: {id} \n Usuario: {nome} \n Mensagem: {dica} \n"

        file.write(linha)

print("Desafio concluído")