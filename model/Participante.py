from interface.PessoaInterface import PessoaInterface
from datetime import date

class Participante(PessoaInterface):

    def __init__(self,nome,nascimento,email):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email

    def __str__(self):
        return "\n\nNome: %s\ne-mail:%s\nnascimento:%s\n"%(self.nome,self.email,self.nascimento)
