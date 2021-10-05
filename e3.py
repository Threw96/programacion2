def e3(n):
    n += 1
    for i in range(n):
        for j in range(i, n):
            print(f"{i} | {j}")

e3(6)