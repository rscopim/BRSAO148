'''
Crie um programa em Python que peça dois números e uma operação matemática (+, -, * ou /), 
e mostre o resultado de acordo com a operação escolhida.
'''
# Criando a classe
class AWS:
    # recebe os valores
    def solicitacao(self):
        self.num1 = int(input("Primeiro numero: "))
        self.num2 = int(input("Segundo numero: "))
        self.operacao = input("Selecione uma operação\n(+)(-)(/)(*):\n")
    # funções para cada operação
    def soma(self):
        self.soma_valor = self.num1 + self.num2
        return f'O valor da sua soma é: {self.soma_valor}'
    def subtracao(self):
        self.subtracao_valor = self.num1 - self.num2
        return f'O valor da sua subtração é: {self.subtracao_valor}' 
    def divisao(self):
        self.divisao_valor = self.num1 / self.num2
        return f'O valor da sua divisao é: {self.divisao_valor}' 
    def multiplicacao(self):
        self.multiplicacao_valor = self.num1 * self.num2
        return f'O valor da sua multiplicação é: {self.multiplicacao_valor}' 
    # Sistema de condição
    def execucao(self):
        if self.operacao == '+':
            return self.soma()
        elif self.operacao == '-':
            return self.subtracao()
        elif self.operacao == '/':
            return self.divisao()
        elif self.operacao == '*':
            return self.multiplicacao()
#objeto
calculadora = AWS()
#Execução da solicitação de dados
calculadora.solicitacao()
#print do valor
print(calculadora.execucao())