nums = []

while True:
    s = input().strip()
    if s == "end":
        break
    try:
        nums.append(float(s))
    except ValueError:
        pass

if nums:
    print(f"ค่าสูงสุด: {max(nums)}")
    print(f"ค่าต่ำสุด: {min(nums)}")
else:
    print("ไม่มีข้อมูล")