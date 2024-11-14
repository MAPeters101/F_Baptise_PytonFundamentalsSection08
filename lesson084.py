
data = {
    'open': 100,
    'high': 110,
    'low': 95,
    'close': 110,
}

print('open' in data)
#print(3.14 in data)
print('open' not in data)
print('x' not in data)

l = [1, 2, 3, 4]
print(3 in l)
print(10 not in l)
print()


print(data)
data.clear()
print(data)
print(len(data))
data = {
    'open': 100,
    'high': 110,
    'low': 95,
    'close': 110,
}
print(len(data))
print()

data_copy = data.copy()
print(data)
print(data_copy)
print(data is data_copy)
data_copy['x'] = 100
print(data)
print(data_copy)
print()

from copy import deepcopy
data_copy = deepcopy(data)
print(data is data_copy)
data_copy['x'] = 100
print(data)
print(data_copy)
print()

d = {
    'a': [1, 2, 3],
    'b': {
        'x': 0,
        'y': 0
    }
}
d_copy = d.copy()
print(d_copy is d)
d['b'] = 100
print(d)
print(d_copy)
print()

d = {
    'a': [1, 2, 3],
    'b': {
        'x': 0,
        'y': 0
    }
}
d_copy = d.copy()
print(d_copy is d)
print(d)
print(d_copy)

d['a'].append(4)
print(d)
print(d_copy)
print()

d_copy = deepcopy(d)
print(d)
print(d_copy)
d_copy['a'].append(5)
print(d)
print(d_copy)
print()


d = dict(a=1, b=2)
print(d)
d = {3.14: 'pi', 2:'even'}
print(d)
#d = dict(2='even')




print(d)

d = {
    'open': 0,
    'high': 0,
    'low': 0,
    'close': 0,
}

print(type(d))

d = dict.fromkeys(['open', 'high', 'low', 'close'], 0)
print(d)

d = dict.fromkeys('python', 1)
print(d)

d = dict.fromkeys(['a', 'a'], 100)
print(d)

symbols = ['AAPL', 'MSFT', 'AAPL', 'MSFT']
d = dict.fromkeys(symbols, 0)
print(d)
print()
l = list(d)
print(l)
print()

d = dict.fromkeys('Python is an awesome language!', 0)
print(d)
print()

d1 = {}
d2 = dict()
print(d1)
print(d2)
print()

transactions = [
    {'item': 'widget', 'trans_type': 'sale', 'quantity': 10},
    {'item': 'widget', 'trans_type': 'sale', 'quantity': 5},
    {'item': 'widget', 'trans_type': 'refund', 'quantity': 2},
    {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
    {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
    {'item': 'license', 'trans_type': 'refund', 'quantity': 1},
]

total_sold = {}
for transaction in transactions:
    item = transaction['item']
    is_sale = True if transaction['trans_type'] == 'sale' else False
    quantity = transaction['quantity']

    if is_sale:
        if item in total_sold:
            total_sold[item] += quantity
        else:
            total_sold[item] = quantity

print(total_sold)

net_sales = {}
for transaction in transactions:
    item = transaction['item']
    is_sale = True if transaction['trans_type'] == 'sale' else False
    quantity = transaction['quantity']

    if not is_sale:
        quantity = -quantity

    if item in net_sales:
        net_sales[item] += quantity
    else:
        net_sales[item] = quantity

print(net_sales)
print('='*80)


total_sold = {}
for transaction in transactions:
    item = transaction['item']
    is_sale = True if transaction['trans_type'] == 'sale' else False
    quantity = transaction['quantity']

    if is_sale:
        if not item in total_sold:
            total_sold[item] = 0
        total_sold[item] += quantity

print(total_sold)
print()

total_sold = {}
print(total_sold.get('widget', 0))

total_sold = {'widget': 10}
print(total_sold.get('widget', 0))













