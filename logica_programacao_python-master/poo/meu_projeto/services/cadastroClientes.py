from models.clientes import Clientes 
def cadastroClt():
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu cpf: ')
    sexo = input('Digite seu sexo: ')
    telefone = input('Digite seu telefone: ')
    email = input('Digite seu email: ')

    clientes = Clientes(nome,cpf,sexo,telefone,email)

    return Clientes