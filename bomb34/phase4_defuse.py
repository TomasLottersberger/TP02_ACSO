arr = [7, 4, 6, 8, 13, 10, 15, 9, 0, 12, 3, 5, 2, 11, 1, 4]
for idx0 in range(16):
    idx = idx0
    count = 0
    total = 0
    while True:
        count += 1
        v = arr[idx]
        total += v
        if v == 15:
            break
        idx = v
    if count == 8:
        print("index0 =", idx0, "suma =", total)