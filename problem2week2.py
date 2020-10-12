def divide(x):
    digits = [int(i) for i in str(x)]
    return digits


if __name__ == "__main__":
    print('input a number')
    n = int(input())
    print(sum(divide(n)))
