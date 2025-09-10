a = int(input('คะแนนเก็บ: '))
b = int(input('คะแนนสอบกลางภาค: '))
c = int(input('คะแนนสอบปลายภาค: '))


if not (0 <= a <= 30):
    print("คะแนนเก็บต้องอยู่ในช่วง 0 ถึง 30")
elif not (0 <= b <= 30):
    print("คะแนนสอบกลางภาคต้องอยู่ในช่วง 0 ถึง 30")
elif not (0 <= c <= 40):
    print("คะแนนสอบปลายภาคต้องอยู่ในช่วง 0 ถึง 40")
else:
    total = a + b + c

    if 80 <= total <= 100:
        print("A")
    elif 75 <= total <= 79:
        print("B+")
    elif 70 <= total <= 74:
        print("B")
    elif 65 <= total <= 69:
        print("C+")
    elif 60 <= total <= 64:
        print("C")
    elif 55 <= total <= 59:
        print("D+")
    elif 50 <= total <= 54:
        print("D")
    elif 0 <= total <= 49:
        print("F")
    else:
        print("Error")