#-------------------------------------#
#Name: Antoine Fox)
#Date: 4/04/24)
#Reference: Assignment 1b for CISP 300)
#Title: Gas cost and distance)
#Inputs: the distance, car miles per gallon, gas cost, electric car miles per tank & ecar tanks per trip
#Process: total gallons and total electricity needed for each car 
#Outputs: total cost for both trips in both cars
#-------------------------------------#
#add comments over each module to make more descriptive

import math




def main():
    distance = float(input("Enter the total number of miles, as the distance of the trip:"))
    ICEmpg = float(input("Enter miles per gallon for your car:"))
    GasCost = float(input("Enter the gas station cost per gallon for that car:"))
    Echarge = float(input("Enter the number of miles your electric vehicle gets off of a full charge:"))
    chargeCost = float(input("Enter the electricity cost for a full charge:"))
    print("--------------------------------------------------------------------------")

    first = calcICEtotal(ICEmpg, GasCost)
    second = calcECarCharges(distance, Echarge)
    third = calcICEgallons(first, distance)
    fourth = calcECarTotal(second, chargeCost)
    fifth = isCheap(third, fourth)
    return


def calcICEtotal(gallons, station):
    totalGCost = gallons * station
    print("If you'd like to take the regular car, the trip would total out to about $", totalGCost + .5)
    print("--------------------------------------------------------------------------")
    return totalGCost + .5

def calcECarCharges(dist, full):
    totalElec = dist / full
    totalElec = math.ceil(totalElec)
    print("You would need about", totalElec, "charges total for your trip")
    print("--------------------------------------------------------------------------")
    return totalElec

def calcICEgallons(dist, cost):
    totalGals = cost/dist
    totalGals = math.ceil(totalGals)
    print("if you'd like to take the car, it would be about",totalGals ,"gallons for your trip")
    print("--------------------------------------------------------------------------")
    return totalGals

def calcECarTotal(electricity, distance):
    totalECost = electricity * distance
    print("In total for the full trip, the Electric Vehicle would cost you about $", totalECost)
    print("--------------------------------------------------------------------------")
    return totalECost

def isCheap(gas, electric):
    if gas < electric:
        print("The vehicle with gas would be about $", electric - gas,"cheaper to use")
    else:
        print("The electric vehicle would probably be a much smoother choice, since it's $", gas - electric,"cheaper")
    return

main()
