def mainMenu():
    print("Escolha uma operação:")
    print("1 - Soma")
    print("2 - Subtracção")
    print("3 - Multiplicação")
    print("4 - Divição")
    print("5 - Potencia")
    print("6 - Raiz Quadrada")
    print("7 - Percentagen")
    print("0 - Sair")
    num = input()
    return num
def soma():
    print("Inserir o numero")
    x = int(input())
    print("Inserir outro numero")
    y = int(input())
    if math.isnan(x) or math.isnan(y):
        print("Tem de ser um numero")
        return
    sum = int(x) + int(y)
    print("A soma desses numeros e " + str(sum))
def sub():
    print("Inserir o numero")
    x = int(input())
    print("Inserir outro numero")
    y = int(input())
    if math.isnan(x) or math.isnan(y):
        print("Tem de ser um numero")
        return
    sum = int(x) - int(y)
    print("A subtração desses numeros e " + str(sum))
def multi():
    print("Inserir o numero")
    x = int(input())
    print("Inserir outro numero")
    y = int(input())
    if math.isnan(x) or math.isnan(y):
        print("Tem de ser um numero")
        return
    sum = int(x) * int(y)
    print("O produto desses numeros e " + str(sum))
def divi():
    print("Inserir o numero")
    x = int(input())
    print("Inserir outro numero")
    y = int(input())
    if x == 0:
        print("Não se pode dividir por 0")
        return
    elif y == 0:
        print("Não se pode dividir por 0")
        return
    elif math.isnan(x) or math.isnan(y):
        print("Tem de ser um numero")
        return
    else:
        sum = int(x) / int(y)
        print("A divição desses numeros e " + str(sum))
def percentage(percent, whole):
  return (percent * whole) / 100.0


import math
import time
import os

num = 1
while(num != 0):
    time.sleep(5)
    os.system("clear")
    num = int(mainMenu())
    if num == 1:
        soma()
    elif num == 2:
        sub()
    elif num == 3:
        multi()
    elif num == 4:
        divi()
    elif num == 5:
        print("Inserir o numero")
        x = int(input())
        print("Inserir a potencia")
        y = int(input())
        if math.isnan(x) or math.isnan(y):
            print("Tem de ser um numero")
            x=1 
            continue
        print("A potencia do numero " + str(x) + " e " + str(pow(x,y)))
    elif num == 6:
        print("Inserir o numero")
        x = int(input())
        if math.isnan(x):
            print("Tem de ser um numero")
            x = 1
            continue
        print("A raiz quadrada do numero " + str(x) + " e " + str(math.sqrt(x)))
    elif num == 7:
        print("Inserir o numero")
        x = int(input())
        print("Insira o valor da percentagem (70%,10%,90%)")
        y = int(input())
        if math.isnan(x) or math.isnan(y):
            print("Tem de ser um numero")
            x=1 
            continue
        print("O valor final e " + str(percentage(y,x)))
    elif num == 0:
        continue
    else:
        print("Insira um numero entre 0-7")
        