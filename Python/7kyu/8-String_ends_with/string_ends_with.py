def solution(text, ending):
    return text[-len(ending):] == ending


print(solution('abc', 'bc') == True)
print(solution('abc', 'd') == False)

# solution
# return string.endswith(ending)
