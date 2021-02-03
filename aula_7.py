# class Calculadora:
#     def __init__(self, num1, num2):
#         self.a = num1
#         self.b = num2

#     def soma(self):
#         return self.a+self.b

#     def subtracao(self):
#         return self.a-self.b

#     def multiplicacao(self):
#         return self.a*self.b

#     def divisao(self):
#         return self.a/self.b

# class Calculadora2:
#     def soma(self, a, b):
#         return a+b

#     def subtracao(self, a, b):
#         return a-b

#     def multiplicacao(self, a, b):
#         return a*b

#     def divisao(self, a, b):
#         return a/b

# class televisao:
#     def __init__(self):
#         self.ligada = False

#     def power(self):
#         if self.ligada:
#             self.ligada = False
#         else:
#             self.ligada = True

# calculadora = Calculadora(10, 2)
# calculadora2 = Calculadora2()

# print(calculadora.soma())
# print(calculadora.subtracao())
# print(calculadora.multiplicacao())
# print(calculadora.divisao())

# print(calculadora2.soma(10, 2))
# print(calculadora2.subtracao(5, 3))
# print(calculadora2.multiplicacao(10, 5))
# print(calculadora2.divisao(100, 2))

# tv = televisao()
# print(tv.ligada)
# tv.power()
# print(tv.ligada)
# tv.power()
# print(tv.ligada)

# class Carro:
#     def __init__(self):
#         self.motor = 'desligado'
#         self.movimento = False

#     def ligar(self):
#         self.motor = 'ligado'
    
#     def acelerar(self):
#         if self.motor == 'ligado':
#             self.movimento = True

#     def carro_em_movimento(self):
#         return self.movimento

# carro = Carro()
# carro.acelerar()
# carro_em_movimento = carro.carro_em_movimento()
# print(carro_em_movimento)

# def minha_funcao(numero):
#     if numero % 2 == 0:
#         return '{} é par'.format(numero)
#     else:
#         return '{} é ímpar'.format(numero)
#     return "zero é neutro"

# resultado = minha_funcao(0)
# print(resultado)