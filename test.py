P = float(input('initial amount '))
if P >= 0:
    r = float(input('interest rate '))
    n = float(input('number of times interest is compounded '))
    t = float(input('number of years '))
    print('final amount', P*(1+r/n)**n*t)
