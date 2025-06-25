# définition de la liste des voyelles reconnues
vowels_list = ["a", "e", "i", "o", "u"]

def get_count(sentence):
    vowels_count = 0 # initialisation du compteur local
    for caractere in sentence:
        if caractere in vowels_list:
            vowels_count += 1
    return vowels_count


result = get_count("bonjour")
print(result)

# Solution en une seule ligne
# return sum(1 for letter in sentence if letter in "aeiouAEIOU")
