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

    print("The minimum number of packages of hot dogs required:", minDogs)
    print("The minimum number of packages of buns required:", minBuns)
    print("The number of hot dogs that will be left over:", dogsLeft)
    print("The number of buns that will be left over:", bunsLeft)


totalHotDogs = getTotalHotDogs()
showResults(totalHotDogs)
