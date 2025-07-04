def find_uniq(arr):
    count = 0
    first_ref_chr = {}
    second_ref_chr = {}
    first_ref_str = ""
    second_ref_str = ""
    for str in arr:
        # print(str)
        processed_chr = set(sorted(list(str.lower())))
        if count == 0:
            first_ref_chr = processed_chr
            first_ref_str = str
            count += 1
        elif processed_chr != first_ref_chr:
            print(processed_chr != first_ref_chr)
            if count ==1:
                second_ref_str = str
                second_ref_chr = processed_chr
                count += 1
            else:
                if processed_chr == second_ref_chr:
                    return first_ref_str
                else:
                    return str
        else:
            count += 1



input = [ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]
output = 'BbBb'
print(find_uniq(input) == output)

# input = [ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]
# output = 'foo'
# print(find_uniq(input) == output)

# itérer sur chaque élément de la liste avec valeur et index
# 1 mettre toutes les lettres en minuscule
# 2 retirer les doublons
# 3 classer par ordre alphabétique
# stocker le resultat dans une variable à la 1ère itération tel que [string_processed, count, [index]]
# le comparer au résultat de l'opération 3 lors des autres itérations
# si string_processed identiques -> count +1 et index.append
    # si plusieurs éléments dans la liste et max count >=2 return l'index de celui avec le min count
# si string_processed différent
    # si max count >= 2 return original string de celui venant d'être testé
    # si count < 2 ajoute un élement dans la liste [[string_processed, count, [index]]
