# -*- coding: utf-8 -*-

from model.Participante import Participante
from datetime import date
import json

def listarParticipantes():
    participantes = []
    #leitura do arquivo
    lista_part = open("participantes.json",'r',encoding="utf8")
    #Parser do JSON em objeto
    jsonObjs = json.loads(lista_part.read())

    #interação do elementos JSON.
    for jsonObj in jsonObjs:
        nome = jsonObj["nome"]
        email = jsonObj["email"]
        data = jsonObj["nascimento"].split("-")
        nascimento = date(int(data[0]),int(data[1]),int(data[2]))
        participante = Participante(nome,nascimento,email)
        print(participante)


def adicionarParticipantes():
    #leitura do arquivo
    lista_part = open("participantes.json",'r',encoding="utf8")

    #Parser do JSON em objeto
    jsonObjs = json.loads(lista_part.read())

    print("\n\n ======== Novo Participante: ======== \n\n")
    nome = input("Digite o nome:")
    nascimento = input("Digite a data de nascimento:")
    email = input("Digite o email:")
    participante = Participante(nome,nascimento,email)

    partJson = {}
    partJson['nome'] = participante.nome
    partJson['email'] = participante.email
    partJson['nascimento'] = participante.nascimento
    jsonObjs.append(partJson)

    with open('participantes.json', 'w', encoding='utf-8') as lista_part:
        json.dump(jsonObjs, lista_part, ensure_ascii=False, indent=4)

    print("\n\n *Novo participante criado.* \n\n")


    return participante

def exibirMenu():
    print("\n======== Menu Participantes ========\n\n"
          "1 - Listar participantes \n"
          "2 - Adicionar participante \n\n"
          "5 - Sair \n")

def main(args = []):

    exibirMenu()
    continuar = True
    participantes = None

    while continuar:
        try:
            opcao = int(input("Digite uma opção: "))

            if opcao == 1:
                listarParticipantes()
                exibirMenu()
            elif opcao == 2:
                adicionarParticipantes()
                exibirMenu()
            elif opcao == 5:
                continuar = False

        except ValueError:
            print("Valor digitado errado")

if __name__ == "__main__":
    main()
