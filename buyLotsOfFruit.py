fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}

def buyLotsOfFruit(orderList):
    price = 0
    for (fruit,amount) in orderList:
        if fruit not in fruitPrices:
            return None
        else:
            price = price + fruitPrices[fruit] * amount
    return price
orderList = [('apples', 2), ('pears', 3), ('limes', 4)]

if buyLotsOfFruit(orderList) is not None:
    print("Cost of %a is %f" % (orderList, buyLotsOfFruit(orderList)))
#print("Cost of %a is %f" % (orderList, buyLotsOfFruit(orderList)))

