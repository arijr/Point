from .Pessoa import Pessoa
from datetime import date
import json


class Participante(Pessoa):

    # participantes = []

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
            print("\n",participante)

    def adicionarParticipantes():

        print("\n\n ======== Novo Participante: ======== \n\n")
        nome = input("Digite o nome:")
        nascimento = input("Digite a data de nascimento:")
        email = input("Digite o email:")
        participante = Participante(nome,email,nascimento)

        #leitura do arquivo
        lista_part = open("participantes.json",'r',encoding="utf8")
        #Parser do JSON em objeto
        jsonObjs = json.loads(lista_part.read())

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
