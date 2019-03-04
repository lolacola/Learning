item1 = float(input('Price for item 1: '))
item2 = float(input('Price for item 2: '))
item3 = float(input('Price for item 3: '))
item4 = float(input('Price for item 4: '))
item5 = float(input('Price for item 5: '))

sum = item1+item2+item3+item4+item5

print('Your total is $', format(sum, ',.2f'), sep='')

salestax = sum * 0.07

print('Your sales tax is: $', format(salestax, ',.2f'), sep='')

total = sum - salestax

print('Your total is: $', format(total, ',.2f'), sep='')