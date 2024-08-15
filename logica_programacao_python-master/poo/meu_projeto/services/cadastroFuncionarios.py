from models.funcionarios import Funcionarios 

def cadastroFun():
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu cpf: ')
    sexo = input('Digite seu sexo: ')
    telefone = input('Digite seu telefone: ')
    email = input('Digite seu email: ')
    matricula = input('Digite sua matricula: ')

    funcionarios = Funcionarios(nome,cpf,sexo,telefone,email, matricula)

    return funcionarios