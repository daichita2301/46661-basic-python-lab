import random

secret = random.randint(1, 20)

count = 0
while True:
    try:
        guess = int(input())
    except:
        break
    count += 1
    if guess > secret:
        print("มากไป")
    elif guess < secret:
        print("น้อยไป")
    else:
        print(f"ถูกต้อง! คุณทายทั้งหมด {count} ครั้ง")
        break
