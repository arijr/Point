# -*- coding: utf-8 -*-

from model.Participante import Participante
from datetime import date
import json

def listarParticipantes():

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
        participante = Participante(nome,email,nascimento)
        print(participante)

def adicionarParticipantes():
    print("\n\n ======== Novo Participante: ======== \n\n")
    nome = input("Digite o nome:")
    nascimento = input("Digite a data de nascimento:")
    email = input("Digite o email:")

    print("\n\n *Novo participante criado.* \n\n")
    participante = Participante(nome,nascimento,email)

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
            elif opcao == 2:
                adicionarParticipantes()
                exibirMenu()
            elif opcao == 5:
                continuar = False

        except ValueError:
            print("Valor digitado errado")

if __name__ == "__main__":
    main()
