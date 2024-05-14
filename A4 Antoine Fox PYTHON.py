print("#--------------------------------------------------------------------------------------------#")
print("# Name:     Antoine Fox                                                                      #")
print("# Date      3/19/24                                                                          #")
print("# Title:    CISP 300 Assignment #4 py                                                        #")
print("# Reference: SoftwareSales example from class                                                 #")
print("# Inputs:   Which terrain type mountain, coastal or flatland, and which terrain              #")
print("# Process:  Calculate how much money per mile based of of which terrain, determine discount based on how many miles, and total cost#")
print("# Outputs:  Print the values that were entered for the input and the results from the module #")
print("#--------------------------------------------------------------------------------------------#")

Mountain = "Mountain"
Coastal = "Coastal"
Flatland = "Flatland"
terrain = str((input("Enter either Mountain, Coastal or Flatland for which terrain: ")))
buildMiles = int(input("Enter how many miles of highway need to be built: "))


# This calcPercentDiscount module determines the cost based on which terrain
def calcPercentDiscount(terrain):

    if terrain == Mountain:
        costPerMile = 60000
        print("Mountainous highway fee is: ", costPerMile,"per mile")
    if terrain == Coastal:
        costPerMile = 50000
        print("Coastal highway fee is: ", costPerMile,"per mile")
    else:
        costPerMile = 35000
        print("Flatland highway fee is: ", costPerMile,"per mile")
    return costPerMile


# This calcDiscMileCost module multiplies the number of miles to be built by the correct discount percentage
def calcDiscMileCost(buildMiles):
    if buildMiles >= 2 and buildMiles <= 15:
        discount = (buildMiles * .10)
        print("The number of miles to be built is: ", buildMiles, "miles with a 10% discount!")
    if buildMiles > 15 and buildMiles <= 60:
        discount = (buildMiles * .25)
        print("The number of miles to be built is: ", buildMiles, "miles with a 25% discount!")
    else:
        discount = (buildMiles * .35)
        print("The number of miles to be built is: ", buildMiles, "miles with a 35% discount!")
    return (discount * buildMiles)

# This costPerTerrainType module multiplies the correct terrain per miles, by discount and number of miles
def costPerTerrainType(cost):
    global terrain
    if terrain == Mountain:
        cost = (discAmount * 60000)
    if terrain == Coastal:
        cost = (discAmount * 50000)
    else:
        cost = (discAmount * 35000)
    return cost

# This ProjectCostReport module(didn't have any real purpose in the end)because the program was already descriptive enough
def ProjectCostReport(disc, total, terrain, booger):
    print(disc)
    print(total)
    print(terrain)
    print(booger)
    return


discAmount = calcDiscMileCost(buildMiles)

totalCost = costPerTerrainType(discAmount)

terrainType = calcPercentDiscount(terrain)

totalAmount = costPerTerrainType(discAmount)
ProjectCostReport(discAmount, totalCost, terrainType, totalAmount)

