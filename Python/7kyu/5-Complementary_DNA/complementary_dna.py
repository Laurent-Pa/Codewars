complementary_symbol = {"A":"T", "C":"G","G":"C","T":"A"}

def DNA_strand(dna):
    complementary_dna = ""
    for symbol in dna:
        if symbol in complementary_symbol:
            complementary_dna += complementary_symbol[symbol]
    return complementary_dna


input = "ATTGC"
output = "TAACG"

result = DNA_strand(input) == output
print(result)

# solution en une ligne
# return dna.translate(str.maketrans("ATCG","TAGC"))

# str.makestrans() crée une table de traduction
# str.translate() applique la traduction
