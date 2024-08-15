from models.clientes import Clientes 
from models.funcionarios import Funcionarios 

def cadastro_pessoa(op):
    nome = input('Digite o nome: ')
    sexo = input('Digite o sexo: ')
    cpf = input('Digite seu cpf: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite seu email: ')

    pessoa = None 
    if op == 1:
        endereco = input('Digite seu endereço: ')
        cliente = Clientes(nome, sexo, cpf, telefone, email)
        cliente.endreco = endereco
        
        return Clientes
    elif op == 2:
        matricula = input('Digite a matricula: ')
        funcao = input('Digite a função: ')
        salario = float(input('Digite o salário: '))
        funcionario = Funcionarios(nome, )
        
        return Funcionarios