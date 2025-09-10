n = int(input())

nums_in_range = []
for _ in range(n):
    num = int(input())
    if 10 <= num <= 50:
        nums_in_range.append(num)

print(f"ค่าที่อยู่ในช่วง 10-50: {nums_in_range}")