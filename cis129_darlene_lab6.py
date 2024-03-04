def getTotalHotDogs():
    attendees = int(input("Number of attendees: "))
    hotDogs = int(input("Number of hot dogs per person: "))
    total = attendees * hotDogs
    return total


def showResults(total):
    DOGS = 10
    BUNS = 8
    dogsLeft = (DOGS - total % DOGS) % DOGS
    minDogs = (total // DOGS) + (0 ** (0 ** dogsLeft))
    bunsLeft = (BUNS - total % BUNS) % BUNS
    minBuns = (total // BUNS) + (0 ** (0 ** bunsLeft))

    print("Minimum packages of hot dogs needed:", minDogs)
    print("Minimum packages of hot dog buns needed:", minBuns)
    print("Hot dogs remaining:", dogsLeft)
    print("Hot dog buns remaining:", bunsLeft)


totalHotDogs = getTotalHotDogs()
showResults(totalHotDogs)
