


nameAndHitDict = {}

removeCharacterList = {
    '"' : ''
}

max_count = 0

with open("../csv/us-500.csv", "r") as file:
    for line in file:
        column_value = line.strip().split('"')
        name = column_value[1]

        if name == 'first_name':
            pass
        else:
            if name in nameAndHitDict:
                nameAndHitDict[name] = nameAndHitDict[name] + 1
            else:
                nameAndHitDict[name] = 1

    for row in nameAndHitDict:
        if max_count < nameAndHitDict[row]:
            max_count = nameAndHitDict[row]





