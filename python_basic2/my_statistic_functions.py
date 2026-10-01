def my_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
    # pass


def my_max(numbers):
    big = 0
    for i in numbers:
        if big < i:
            big = i
    return big
    # pass


def my_min(numbers):
    small = numbers[0]
    for i in numbers:
        if i < small:
            small = i
    return small
    # pass


def my_average(numbers):
    total = 0
    for i in numbers:
        total += i
    return int(total / len(numbers))
    # pass


def main():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21]
    print(my_sum(numbers))
    print(my_max(numbers))
    print(my_min(numbers))
    print(my_average(numbers))


if __name__ == "__main__":
    main()
