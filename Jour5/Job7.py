def check_chain(chain1, chain2):
    if chain1 == chain2:
        return "1"
    else:
        if '*' in chain2:
            splits = chain2.split('*')
            if not chain1.startswith(splits[0]):
                return "0"
            else:
                chain2 = chain2[len(splits[0]):]
                for split in splits[1:]:
                    if split in chain1:
                        chain1 = chain1[chaine1.find(split) + len(split):]
                    else:
                        return "0"
                else:
                    return "1"
        else:
            return "0"


chaine1 = input("Entrez la première chaîne : ")
chaine2 = input("Entrez la deuxième chaîne : ")
print(f"La première suite {chaine1} et la deuxième suite {chaine2} donne: {check_chain(chaine1, chaine2)}")
