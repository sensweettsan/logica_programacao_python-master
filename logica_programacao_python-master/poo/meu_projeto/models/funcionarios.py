from models.pessoas import Pessoa

class Funcionarios(Pessoa):
    def __init__(self, nome: str, sexo: str, cpf: str, telefone: str, email: str, matricula: str, funcao: str, caixa: str, salario: float):
        super().__init__(nome, sexo, cpf, telefone, email)
        self.matricula = matricula
        self.funcao = funcao
        self.caixa = caixa
        self.salario = salario

     
       
      
       
    
      


        