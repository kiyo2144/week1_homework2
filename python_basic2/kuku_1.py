def create_kuku_table():
    # 9行9列の九九表を2次元リストで返す
    table = []
    count1 = 1

    while count1 <= 9:
        row = []
        count2 = 1
        while count2 <= 9:
            row.append(count1 * count2)
            count2 += 1
        table.append(row)
        count1 += 1

    return table
