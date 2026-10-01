def format_kuku(rows, columns):
    # 各行の文字列をリストで返す
    # pass

    table = []

    for i in range(1, rows + 1):
        cell = []
        for j in range(1, columns + 1):
            cell.append(f"{j} x {i} =  {i*j} | ")
        table.append("".join(cell))

    return table


def main():
    rows = int(input("行数を入力してください: "))
    columns = int(input("列数を入力してください: "))
    # create_kuku_table() の結果を表示する

    table = format_kuku(rows, columns)

    for row in table:
        for product in row:
            print(f"{product} ", end="")

        print()


if __name__ == "__main__":
    main()
