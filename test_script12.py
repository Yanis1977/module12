per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму:"))

TKB = int((per_cent['ТКБ']) * (money / 100))

SKB = int((per_cent['СКБ']) * (money / 100))

VTB = int((per_cent['ВТБ']) * (money / 100))

SBER = int((per_cent['СБЕР']) * (money / 100))

deposit = [TKB, SKB, VTB, SBER]

max = deposit[0]

for i in range(1, len(deposit)):

    if deposit[i] > max:
        max = deposit[i]

print('максимальный доход', max)

print(deposit)

