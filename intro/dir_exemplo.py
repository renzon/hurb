'''
Estudo do dir para descobrir se extend existe na string
'''

print(dir(str))


class Formulario:
    def __init__(self, nome=None, cpf=None):
        print('Inicializando Formulário')
        self.cpf = cpf
        self.nome = nome

    def imprimir_dados(self):
        print(id(self), self.nome, self.cpf)


renzo = Formulario('Renzo', 'foo')
bia = Formulario()
bia.nome = 'Bia'

print(F'Id do Renzo:  {id(renzo)} , {renzo.nome} ,  {renzo.cpf}')
renzo.imprimir_dados()
print(f'Id da Bia: {id(bia)}')
bia.imprimir_dados()

if renzo.nome == None and renzo.cpf == None:
    print('faltando nome e cpf')
elif renzo.cpf == None:
    print('faltando cpf')
elif renzo.nome == None:
    print('faltando nome')
else:
    print('Form ok!')
