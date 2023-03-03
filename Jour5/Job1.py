def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)


number = int(input("Nombre: "))
result = factorielle(number)
print(f"Le factoriel de {number} est {result}.")
