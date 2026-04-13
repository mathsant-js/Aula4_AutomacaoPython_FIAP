for num in range(2, 2001):
    isPrimo = True

    for i in range(2, num):
        if num % i == 0:
            isPrimo = False
            break

    if isPrimo:
        print(num)