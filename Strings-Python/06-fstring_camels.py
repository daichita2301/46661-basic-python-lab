s = input().strip()

num = ""
text = ""
for c in s:
    if c.isdigit() or c == ".":
        num += c
    else:
        text += c


years = int(float(num) // 10)
animals = float(num) % 10

print(f"In {years} years I have spotted {animals} {text}.")