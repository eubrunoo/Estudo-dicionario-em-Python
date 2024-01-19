import os

def limpeza():
    os.system('cls')

try:
    limpeza()
    nome_usuario = input('Qual seu nome? ')
    limpeza()
    idade_usuario = int(input('Qual a sua idade? '))
    limpeza()
    cidade_usuario = input('Qual sua cidade? ')
    limpeza()
    profissao_usuario = input('Qual sua profissão? ')

except ValueError:
    limpeza()
    print('Verifique se é um valor inteiro.')

dados_usuario = [{'Nome': nome_usuario, 'Idade': idade_usuario, 'Cidade': cidade_usuario, 'Profissão': profissao_usuario}]

chaves_verificar = ['Nome', 'Cidade', 'Profissão']

for chave in chaves_verificar:
    if not dados_usuario[0][chave].isalpha():
        print(f'O dado - {dados_usuario[0][chave]} - fornecido não é composto apenas por letras.')

if not dados_usuario[0]['Nome']['Cidade']['Profissão'].isalpha():
    print('Verifique se não utilizou valores inteiros em perguntas não referentes a idade.')

limpeza()
print(f'A idade de {dados_usuario[0]["Nome"]} é {dados_usuario[0]["Idade"]}\n')