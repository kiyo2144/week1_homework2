def create_kuku_table(rows, columns):
    # rows行、columns列の掛け算表を2次元リストで返す

    table = []

    for i in range(1, rows + 1):
        row = []
        for j in range(1, columns + 1):
            row.append(i * j)
        table.append(row)

    return table


def main():
    rows = int(input("行数を入力してください: "))
    columns = int(input("列数を入力してください: "))
    # create_kuku_table() の結果を表示する

    table = create_kuku_table(rows, columns)

    for row in table:
        for product in row:
            print(f"{product} ", end="")

        print()


if __name__ == "__main__":
    main()
