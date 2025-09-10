amount = float(input("Enter amount: "))

if amount >= 2000:
    discount = amount * 0.15
elif amount >= 1000:
    discount = amount * 0.10
elif amount >= 500:
    discount = amount * 0.05
else:
    discount = 0

net_price = amount - discount

print(net_price)