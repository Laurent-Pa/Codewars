def find_uniq(arr):
    def processing_string(input):
        """Letters in downcase, unique and sorted for easier visual comparison"""
        return "".join(set(sorted(list(input.lower()))))


    first_string = processing_string(arr[0])
    second_string = processing_string(arr[1])
    if first_string != second_string:
        # l'intru est dans l'un des 2 premiers éléments
        third_string = processing_string(arr[2])
        if first_string == third_string:
            return arr[1]
        else:
            return arr[0]
    else:
        # l'intru n'est pas dans les 2 premiers éléments, on itère  sur le reste
        reference_string = first_string
        for str in arr:
            if processing_string(str) != reference_string:
                return str


input = [ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]
output = 'BbBb'
print(find_uniq(input) == output)
