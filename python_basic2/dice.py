import random


def roll_dice(sides, times):
    results = []
    for _ in range(times):
        results.append(random.randint(1, sides))
    return results
    # pass


def main():
    sides = int(input("サイコロの面の数は?: "))
    times = int(input("何回振りますか?: "))

    print(roll_dice(sides, times))


if __name__ == "__main__":
    main()
