from interface.PessoaInterface import PessoaInterface
from datetime import date


class Pessoa(PessoaInterface):

    def __init__(self, nome, email, nascimento):
        self.nome = nome
        self.email = email
        self.nascimento = nascimento

    def cadastrar(self):
        print('Cadastrando...\n')
        p = Pessoa(self.nome,self.email,self.nascimento)

        return p

    def __str__(self):
        pessoa = 'Nome: %s \nEmail: %s \nNascimento: %s' %(self.nome,self.email,self.nascimento)

        return pessoa

    def __eq__(self, other):
        return (self.nome == other.nome) \
            and (self.email == other.email) \
            and (self.nascimento == other.nascimento)

# p = Pessoa('Ari', 'ari@teste', date(1986,12,22))
# p2 = Pessoa('Jose','jose@mail',date.today())

# print(p)
# print(p2)

# print(p==p2)