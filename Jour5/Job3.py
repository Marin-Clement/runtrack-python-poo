def string_length(s):
    if s == '':
        return 0
    else:
        return 1 + string_length(s[1:])


s = "Leo est nul sur zac"
length = string_length(s)
print(f"La chaîne '{s}' a une longueur de {length} caractères.")
