from model.Pessoa import Pessoa
from datetime import date

import json

   
def exibirMenu():
    print("\nMenu de participantes: \n\n"
            "1 - Listar participantes \n"
            "2 - Adicionar participante \n"
            "3 - Sair\n")

def main(args = []):
    
    exibirMenu()

    continuar = True

    while continuar:
        try:
            opcao = int(input("Digite a opção: "))

            if (opcao == 1):
                print("Listar participantes")
            elif (opcao == 2):
                print("Adicionar participante")
            elif (opcao == 3):
                print("Sair")
                continuar = False
            else:
                print("Opção inválida!")
        
        except ValueError:
            print("Digite um valor válido")



if __name__ == '__main__':
    main()

