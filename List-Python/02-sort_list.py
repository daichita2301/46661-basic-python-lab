n = int(input())
number = []
for i in range(n):
    num = int(input())
    number.append(num)
print("ลิสต์เดิม: ", number)
number.sort()
print("ลิสต์เรียงแล้ว: ", number)