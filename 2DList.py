
numbers = [1, 1, 1, 2, 2, 2]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
