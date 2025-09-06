def show_table(n, limit):
    i = 1
    while i <= limit:
        print(f"{n} x {i} = {n*i}")
        i += 1

n = int(input("n = ").strip())
limit = int(input("limit = ").strip())
show_table(n, limit)