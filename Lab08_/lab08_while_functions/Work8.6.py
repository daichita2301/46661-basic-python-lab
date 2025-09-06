def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b

while True:
    print("1. บวกเลขสองจำนวน")
    print("2. ลบเลขสองจำนวน")
    print("3. คูณเลขสองจำนวน")
    print("4. ออก")

    choice = int(input().strip())

    if choice == 4:
        print("จบโปรแกรม")
        break

    a = float(input().strip())
    b = float(input().strip())

    if choice == 1:
        print(f"ผลลัพธ์: {add(a, b)}")
    elif choice == 2:
        print(f"ผลลัพธ์: {sub(a, b)}")
    elif choice == 3:
        print(f"ผลลัพธ์: {mul(a, b)}")
    else:
        print("เลือกไม่ถูกต้อง")