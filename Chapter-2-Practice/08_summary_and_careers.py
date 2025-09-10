a = float(input("Bill amount: "))
b = float(input("Tips percentage: "))
c = int(input("people: "))

tip = a * (b / 100)
total = a + tip
each = total / c

print(f"Each person pays: {each:.2f}")