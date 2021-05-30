def factors(b):
    """
    Find the factors of an integer
    """
    ret = []
    for i in range(1, b + 1):
        if b % i == 0:
            ret.append(i)
    return ret


def main():
    b = float(input('Your Number Please: '))

    if b <= 0 or (not b.is_integer()):
        print('Please enter a positive integer')
        exit(1)

    for i in factors(int(b)):
        print(i)


if __name__ == '__main__':
    main()
