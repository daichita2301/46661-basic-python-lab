s = input().strip()
mid = len(s) // 2
a = s[:mid].lower()
b = s[mid:].lower()

if a < b:
    print("A comes before B")
elif a > b:
    print("A comes after B")
else:
    print("A equals B")