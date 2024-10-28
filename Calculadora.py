from imghdr import test_rgb
from importlib.metadata import pass_none
from logging import shutdown

def soma(x, y):
    return x + y

def subtração(x, y):
    return x - y

def divisão(x, y):
    return x / y

def multiplicação(x, y):
    return x * y

history = []

def calculadora():
    num1 = (input("Num1: "))
    try:
        val = float(num1)
        print('Valid Num')
    except ValueError :
        print('Invalid Num Silly')
    operação2 = input('operação: +, -, *, /: ')
    num2 = (input("Num2: "))
    try:
        val = float(num2)
        print('Valid Num')
    except ValueError :
        print('Invalid Num Silly')

    if operação2 == "+":
        result = soma(num1, num2)
        print("soma: " + str(result))
        history.insert(0,result)

    if operação2 == "-":
        result1 = subtração(num1, num2)
        print("subtração: " + str(result1))
        history.insert(0, result1)

    if operação2 == "/":
        result2 = divisão(num1, num2)
        print("divisão: " + str(result2))
        history.insert(0, result2)

    if operação2 == "*":
        result3 = multiplicação(num1, num2)
        print("multiplicação: " + str(result3))
        history.insert(0, result3)

    if len(history) >=6:
      history.pop(5)

    e = input('Show History ?')
    if e == 'yes':
        print(list(history))
    else:
        pass

    stop = input('stop? - yes/no:')

    if stop == 'yes':
        result = shutdown()
    else:
        calculadora()

calculadora()