def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x, n//2)**2
    else:
        return x * power(x, n-1)


x = int(input("Entrez un nombre : "))
n = int(input("Entrez l'exposant : "))
result = power(x, n)
print(f"{x}^{n} = {result}")
