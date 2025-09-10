n = int(input())
number = []
for i in range(n):
    num = int(input())
    number.append(num)
max = max(number)
min = min(number)
print("มากที่สุด:", max)
print("น้อยที่สุด:", min)