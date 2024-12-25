class Potion:
    def __init__(self, recover, price, sell_price):
        self.recover = recover
        self.price = price
        self.sell_price = sell_price

small = Potion(50, 10, 5)
medium = Potion(70, 15, 8)
large = Potion(100, 20, 10)

print(f"Small Potion -Recovery: {small.recover} -Buy: {small.price}G")
print(f"Medium Potion -Recovery: {medium.recover} -Buy: {medium.price}G")
print(f"Large Potion -Recover: {large.recover} -Buy: {large.price}G")
      