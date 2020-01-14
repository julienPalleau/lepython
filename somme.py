def somme(a, b=0, *arg):
    sum = 0
    for num in arg:
        sum += num
    sum += a+b

    return sum


print(somme(2))
