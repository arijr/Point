from interface.participanteInterface import participanteInterface
from datetime import date


class Participante(ParticipanteInterface):

    def __init__(self, nome, email, nascimento):
        self.nome = nome
        self.email = email
        self.nascimento = nascimento

    def __str__(self):
        pessoa = 'Nome: %s \nEmail: %s \nNascimento: %s' %(self.nome,self.email,self.nascimento)

        return pessoa

    def __eq__(self, other):
        return (self.nome == other.nome) \
            and (self.email == other.email) \
            and (self.nascimento == other.nascimento)


    def cadastrar(self):
        print('Cadastrando...\n')
        pessoa = Pessoa(self.nome,self.email,self.nascimento)

        return pessoa

    def listar(self):
        pass

    def remover(id):
        pass

    def atualizar(self,Participante):
