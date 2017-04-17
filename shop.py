class FruitShop:

    def __init__(self, name, fruitPrices):
        """
            name: Name of the fruit shop
            
            fruitPrices: Dictionary with keys as fruit 
            strings and prices for values e.g. 
            {'apples':2.00, 'oranges': 1.50, 'pears': 1.75} 
        """
        self.fruitPrices = fruitPrices
        self.name = name
        print('Welcome to %s fruit shop'.format(name))
        
    def getCostPerPound(self, fruit):
        """
            fruit: Fruit string
        Returns cost of 'fruit', assuming 'fruit'
        is in our inventory or None otherwise
        """
        if fruit not in self.fruitPrices:
            return None
        return self.fruitPrices[fruit]
        
    def getPriceOfOrder(self, orderList):
        price = 0
        for (fruit, amount) in orderList:
            if fruit not in self.fruitPrices:
                return None
            else:
                price = price + self.fruitPrices[fruit] * amount
        return price

    def getName(self):
        return self.name
