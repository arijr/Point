# -*- coding: utf-8 -*-
from model.Participante import Participante


def main(args = []):

    Participante.exibirMenu()
    continuar = True

    while continuar:
        try:
            opcao = int(input("Digite uma opção: "))

            if opcao == 1:
                Participante.listarParticipantes()
                Participante.exibirMenu()
            elif opcao == 2:
                Participante.adicionarParticipantes()
                Participante.exibirMenu()
            elif opcao == 5:
                continuar = False

        except ValueError:
            print("Valor digitado errado")
            Participante.exibirMenu()

if __name__ == "__main__":
    main()
