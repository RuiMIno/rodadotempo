
# Regras anos bissextos:    inicio >> 1600 e respeita prioridade das regras na ordem apresentada
#       1 regra >> de 400 em 400 anos  E BISSEXTO                               >>  1600, 2000, 2400...
#       2 regra >> de 100 em 100 anos  NAO E BISSEXTO   >> excepto regra 1      >>  1700, 1800, 1900, 2100...
#       3 regra >> de   4 em   4 anos  E BISSEXTO       >> excepto regras 1 e 2
#   A funcao predente encontrar todos os anos bissextos dentro de um intervalo onde so se aplica a regra 3

def criaAnosBi():
    anosTot = []
    anosSeg = []
    anoBiRef = 1912
    rangeIni = 1900
    ajuste = abs(rangeIni - anoBiRef)
    for x in range(rangeIni, 2100):
        if divmod(x, 400)[1] == 0:
            anosTot.append(x)
            if x == anoBiRef:
                anosSeg.append(x)
            elif (x > anoBiRef) and ((x - ajuste) % 28) == 0:
                anosSeg.append(x)
        elif x % 4 == 0:
            if divmod(x, 100)[1] != 0:
                anosTot.append(x)
                if x == anoBiRef:
                    anosSeg.append(x)
                elif (x > anoBiRef) and ((x - ajuste) % 28) == 0:
                    anosSeg.append(x)
    print(anosTot)
    print(anosSeg)
#criaAnosBi()

# rules for description O: Output   I: input
def WhatIsTheWeekday()
    inpDia = 23                  #inpDia = int(input('Dia: '))           I: day
    inpMes = 11                  #inpMes = int(input('Mes: '))           I: month
    inpAno = 1973                #inpAno = int(input('Ano: '))           I: year

    import calendar
    calendText = calendar.TextCalendar()            # Create a Calendar in Text format
    a = calendText.prmonth(inpAno, inpMes)          # OP: calendar for I(year,month)

    calend2 = calendar
    numDiaSem = calendar.weekday(inpAno, inpMes, inpDia)             # weekday. a number in range 0 - 6
    nomeDiaSem = calend2.day_name[numDiaSem]                         # O: weekday name for a number in range 0 - 6
    nomeMes = calend2.month_name[inpMes]                             # O: month name for a number in range 1 - 12
    print()
    print('Day ', inpDia, ' of ', nomeMes, ' in ', inpAno, ' was a: ', nomeDiaSem )

# How to find the Weekday any day from 1900 to 2100
# The estrategy is based in the knowledge of the especial years which hold a specific caracteristic:
#       - be a leap year wich first weekday of the years is a Monday. they happen any 28 years
#
