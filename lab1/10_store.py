goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

lamp_code = goods['Лампа']
lamp_qty = store[lamp_code][0]['quantity']
lamp_price = store[lamp_code][0]['price']
lamp_cost = lamp_qty * lamp_price
print('Лампа - ',lamp_qty,' шт, стоимость ',lamp_cost,' руб')

table_code = goods['Стол']
table_qty1 = store[table_code][0]['quantity']
table_price1 = store[table_code][0]['price']
table_cost1 = table_qty1 * table_price1
table_qty2 = store[table_code][1]['quantity']
table_price2 = store[table_code][1]['price']
table_cost2 = table_qty2 * table_price2
table_qty = table_qty1 + table_qty2
table_cost = table_cost1 + table_cost2
print('Стол - ',table_qty,' шт, стоимость ',table_cost,' руб')

sofa_code = goods['Диван']
sofa_qty1 = store[sofa_code][0]['quantity']
sofa_price1 = store[sofa_code][0]['price']
sofa_cost1 = sofa_qty1 * sofa_price1
sofa_qty2 = store[sofa_code][1]['quantity']
sofa_price2 = store[sofa_code][1]['price']
sofa_cost2 = sofa_qty2 * sofa_price2
sofa_qty = sofa_qty1 + sofa_qty2
sofa_cost = sofa_cost1 + sofa_cost2
print('Диван - ',sofa_qty,' шт, стоимость ',sofa_cost,' руб')

chair_code = goods['Стул']
chair_qty1 = store[chair_code][0]['quantity']
chair_price1 = store[chair_code][0]['price']
chair_cost1 = chair_qty1 * chair_price1
chair_qty2 = store[chair_code][1]['quantity']
chair_price2 = store[chair_code][1]['price']
chair_cost2 = chair_qty2 * chair_price2
chair_qty3 = store[chair_code][2]['quantity']
chair_price3 = store[chair_code][2]['price']
chair_cost3 = chair_qty3 * chair_price3
chair_qty = chair_qty1 + chair_qty2 + chair_qty3
chair_cost = chair_cost1 + chair_cost2 + chair_cost3
print('Стул - ',chair_qty,' шт, стоимость ',chair_cost,' руб')
