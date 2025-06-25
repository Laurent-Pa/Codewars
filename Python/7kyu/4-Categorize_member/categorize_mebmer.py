input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

def open_or_senior(data):
    categories = []
    for (age, handicap) in data:
        if age >= 55 and handicap > 7:
            categories.append("Senior")
        else:
            categories.append("Open")
    return categories

test_completed = open_or_senior(input) == output
print(test_completed)

# Solution en une ligne
# return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
