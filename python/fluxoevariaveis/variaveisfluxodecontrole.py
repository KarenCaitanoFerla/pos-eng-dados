#Exercícios genericos de testes de conhecimento da pós-graduação
#CONHECIMENTO VARIAVEIS E FLUXO DE CONTROLE
#Como são códigos curtos e são apenas para demonstrar conhecimento, optei por colocá-los todos no mesmo arquivo.

from datetime import datetime, timedelta 

#Pergunta 1 __________________________________________________________________________________________________________________
#Escrever um programa que leia 3 valores A, B e C, e os escreva em ordem crescente. 
valores = []
for num in range(3):
    x = int(input('Digite {0}º número inteiro:'.format(num+1)))
    valores.append(x)

valores.sort()

print('Valores ordenados:')
for valor in valores:
    print(valor)

#Pergunta 2 __________________________________________________________________________________________________________________
#Faça um programa que leia uma data qualquer (dia, mês e ano) e calcule a data do próximo dia.
#  Lembre-se que em anos bissextos o mês de fevereiro tem 29 dias.
#(Dica: um ano é bissexto quando for divisível por 4)
dia = int(input('Digite o dia (número inteiro):'))
mes = int(input('Digite o mês (número inteiro):'))
ano = int(input('Digite o ano (número inteiro):'))

data = datetime.date(ano, mes, dia)
amanha = data + datetime.timedelta(days = 1)

print('O próximo dia será {0}'.format(amanha))

#Pergunta 3 __________________________________________________________________________________________________________________
#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e
#  estado civil seja “CASADA”, solicitar o tempo de casada (anos).

nome = input("Informe seu nome: ")
sexo = input("Informe seu sexo, F ou M :")
civil = input("Informe seu estado civil: Solteiro, Casado, Viuvo: ")
if sexo.upper() == 'F' and civil.upper() == 'CASADO':
    tempo = input("É casado a quanto tempo? ")
else:
    tempo = 'Não há'

print(f'nome: {nome}; sexo: {sexo}, estado civil: {civil}, tempo de relacionamento: {tempo}')

#Pergunta 4 __________________________________________________________________________________________________________________
#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois,
#  caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado
#  para uma variável C e mostrar seu conteúdo na tela. 

a = int(input("Informe um numero inteiro para A: "))
b = int(input("Informe um numero inteiro para B: "))
if a == b:
    c = a + b
else:
    c = a * b

print("Resultado: ", c)

#Pergunta 5 ____________________________________________________________________________________________________________________
#Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado. 

num = float(input("Digite um número positivo, ou negativo: "))
if num > 0:
    result = num * 2
elif num < 0:
    result = num * 3
else:
    result = f'Numero neutro: {num}'
print(f'O resultado foi: {result}')

#Pergunta 6 __________________________________________________________________________________________________________________
#Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação. 

num = int(input("Informe um numero inteiro: "))
divi = num % 2
if divi == 0:
    result = num + 5
    print(f"Numero par ({num})! Com a soma ficou {result}")
else:
    result = num + 8
    print(f"Numero ímpar ({num})! Com a soma ficou {result}")

#Pergunta 7 __________________________________________________________________________________________________________________
#O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar umaindicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / ( altura )2
#Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo.
#IMC em adultos Condição Abaixo
#de 18,5 Abaixo do peso
#Entre 18,5 e 25 Peso normal
#Entre 25 e 30 Acima do peso
# Acima de 30 obeso

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
 
imc = peso / altura**2

if imc < 18.5:
    print("Abaixo do peso!")
elif 18.5 < imc < 25:
    print("Peso normal!")
elif 25 < imc < 30:
    print("Acima do peso!")
elif imc > 30:
    print("Obeso!")

#Pergunta 8 __________________________________________________________________________________________________________________
# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da
#  condição de pagamento. Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.

# Código Condição de pagamento

# À vista em dinheiro ou cheque, recebe 10% de desconto
# À vista no cartão de crédito, recebe 15% de desconto
# Em duas vezes, preço normal de etiqueta sem juros
# Em duas vezes, preço normal de etiqueta mais juros de 10%

valor = float(input("Qual o valor da compra? "))

condicao = input("Qual a forma de pagamento? digine a letra da opção. \na)À vista em dinheiro ou cheque \nb)À vista no cartão de crédito \nc)Em duas vezes, sem juros. \nd) Em duas vezes, com juros.\nResposta: ")

if 'a' in condicao:
    desc = valor * 0.1
    result = valor - desc
elif 'b' in condicao:
    desc = valor * 0.15
    result = valor - desc
elif 'c' in condicao:
    print(f'Ficam duas parcelas de: {valor / 2}')
elif 'd' in condicao:
    juros = valor * 0.1
    result = valor + juros
    print(f'Ficam duas parcelas de: {result / 2}')

#Pergunta 9 __________________________________________________________________________________________________________________
# Faça um programa, utilizando estrutura de condição, que receba um número real, digitado pelo usuário e mostre o menu para selecionar o tipo de cálculo que deve ser realizado com base nos códigos abaixo:

# 101- Raiz quadrada
# 102- A metade
# 103- 10% do número
# 104- O dobro

num = float(input("Digite um numero real: "))
recebe = int(input("Voce quer receber: \n101- Raiz quadrada \n102- A metade \n103- 10% do número \n104- O dobro\nDigite o numero de sua escolha: "))

if recebe == 101:
    result = num ** 0.5
    print(f'Raiz quadrada de {num} é: {result}')
elif recebe == 102:
    result = num / 2
    print(f'A metade de {num} é: {result}')
elif recebe == 103:
    result = num * 0.1
    print(f'10% de {num} é: {result}')
elif recebe == 104:
    result = num * 2
    print(f'O dobro de {num} é: {result}')

