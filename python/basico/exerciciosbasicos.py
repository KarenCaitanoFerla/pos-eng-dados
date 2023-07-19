#Exercícios genericos de testes de conhecimento da pós-graduação
#CONHECIMENTO BÁSICO PYTHON
#Como são códigos curtos e são apenas para demonstrar conhecimento, optei por colocá-los todos no mesmo arquivo.

import math
from fractions import Fraction

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
val_hora = input("Quanto você ganha por hora? ")
horas_mes = input("Você trabalha quantas horas por mes? ")

salario = val_hora + horas_mes

print("O salário mensal é: ", salario)



#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = input("Qual a sua altura? ")
peso_h = (72.7 * float(altura)) - 58
peso_m = (62.1 * float(altura)) - 44.7

print(f'O peso ideal para a altura {altura}: \npara homens é de: {peso_h} \npara as mulheres é de: {peso_m}')



#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu
#  salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
#  faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

val_hora = int(input("Quanto voce ganha por hora? "))
hr_mes = int(input("Quantas horas você trabalha no mês? "))
sal_bru = val_hora * hr_mes
imposto_renda = sal_bru * 0.11
inss = sal_bru * 0.08
sindi = sal_bru * 0.05
sal_liqui = sal_bru - (imposto_renda + inss + sindi)
print(f'+ Salário Bruto : R${sal_bru}\n- IR (11%) : R${imposto_renda}\n- INSS (8%) : R${inss}\n- Sindicato ( 5%) : R${sindi}\n = Salário Liquido : R${sal_liqui}')



#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area_pintada = int(input("Quantos metros quadrados serão pintados? "))
litro = area_pintada / 3
lata = litro / 18
comprar = math.ceil(lata)
preco = comprar * 80.00
print(f'Para pintar {area_pintada}m², você precisará comprar: {comprar} latas! O valor ficará: R${preco}')



#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area_pintada = int(input("Quantos metros quadrados serão pintados? "))
litro = area_pintada / 6
lata = litro / 18
#lata de 18 litros com 10% de folga:
lata_folga = lata + (lata * 0.10)
galao = litro / 3.6
galao_folga = math.ceil(galao + (galao * 0.10))

if lata_folga >= 1:
    decimais = lata_folga - int(lata_folga)
    if decimais == 0:
        valor = lata_folga * 80.0
        print(f'''Você deverá comprar {lata} lata(s) de 18 litros para pintar {area_pintada}m².\n
              O valor ficará R${valor}.\n
              Lembrando que nesse valor já foi calculado uma folga de 10% do produto.\n
              Com rendimento de 1 litro para cada 6 metros quadrados''')
    else:
        litros_restantes = decimais * 18
        quantas_lata_p = math.ceil(litros_restantes / 3.6)
        quantas_lata_g = int(lata_folga)
        valor_total = (quantas_lata_p * 25.0) + (quantas_lata_g * 80.0)
        print(f'''Você deverá comprar: \n{quantas_lata_g} latas de 18 litros e {quantas_lata_p} latas de 3.6 litros .\n
            O valor total ficará: R${valor_total}.
            Lembrando que nesse valor já foi calculado uma folga de 10% do produto.\n
            Com rendimento de 1 litro para cada 6 metros quadrados''')
else:
    valor_total_p = galao_folga * 25.0
    print(f'''Você deverá comprar {galao_folga} latas de 3.6 litros.\n
        O Valor total ficará: R${valor_total_p}.\n
        Lembrando que nesse valor já foi calculado uma folga de 10% do produto.\n
        Com rendimento de 1 litro para cada 6 metros quadrados''')



#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#  calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tam_arq = int(input("Qual o tamanho do arquivo para download (em MB)? "))
velocidade = int(input("Qual a velocidade de um link de Internet (em Mbps)? "))
tempo_download = (tam_arq / velocidade) / 60
print(f"O tempo aproximado para download será de {tempo_download} minutos!")



#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Faça um Programa que peça as 4 notas bimestrais e mostre a média
notaum = float(input("Qual a nota do primeiro bimestre? "))
notadois = float(input("Qual a nota do segundo bimestre? "))
notatres = float(input("Qual a nota do terceiro bimestre? "))
notaquatro = float(input("Qual a nota do quarto bimestre? "))

media = (notaum + notadois + notatres + notaquatro) / 4
print(f"A média anual foi de : {media}")

