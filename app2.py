#coding: utf8

from model.Pessoa import Pessoa
from datetime import date

import json

def main(args = []):
    while True:
        try:
            pessoas = []

            #LÊ ARQUIVO 
            arq = open("pessoas.txt",'r',encoding="utf8")

            #Parser do JSON em Objeto
            jsonObjs = json.loads(arq.read())

            #interação dos objetos json
            for jsonObj in jsonObjs:
                nome = jsonObj["nome"]
                email = jsonObj["email"]
                data = jsonObj["nascimento"].split("-")
                nascimento = date(int(data[0]),int(data[1]),int(data[2]))
                pessoa = Pessoa(nome,email,nascimento)
                print(pessoa)
                pessoas.append(pessoa)

            pedro = Pessoa('Pedro','pedro@mail.com','2000-12-11')
            pessoas.append(pedro)

            pedroJson = {}
            pedroJson['nome'] = pedro.nome
            pedroJson['email'] = pedro.email
            pedroJson['nascimento'] = pedro.nascimento
            jsonObjs.append(pedroJson)

            with open('pessoas.txt', 'w', encoding='utf-8') as arq:
                json.dump(jsonObjs, arq, ensure_ascii=False, indent=4)

            break
        except FileNotFoundError as err:
            print(err)
            print("Arquivo não encontrado!")

if __name__ == '__main__':
    main()