#-------------------------------------
#Name: Antoine Fox
#Date: 4/04/24
#Reference: none
#Title: Customer info update
#Inputs: Premium, diesel and regular gas sold and cost per gallon
#Process: regular, premium and diesel income also the total sales
#Outputs: total income for the month, total taxes for the month, gross income for the month
#-------------------------------------

import math


#Add comments over each to make them look nicer
def printIncomeReport():
    premGas = float(input("Enter the cost per gallon for premium gas:"))
    regGas = float(input("Enter the cost per gallon for regular gas:"))
    deezGas = float(input("Enter the cost per gallon for diesel gas:"))
    premSold = float(input("Enter the number of premium gallons sold:"))
    regSold = float(input("Enter the number of regular gallons sold:"))
    deezSold = float(input("Enter the number of diesel gallons sold:"))

    first = calcPremiumIncome(premGas, premSold)
    second = calcRegIncome(regGas, regSold)
    third = calcDiesIncome(deezGas, deezSold)
    fourth = calcTotalSales(first, second, third)
    fifth = calcTotalTaxes(fourth)
    sixth = calcBusinessIncome(fourth, fifth)

def calcPremiumIncome(costPG, gasSold):
    totalPrem = costPG * gasSold
    print("The total earned income earned from PREMIUM gas is $", totalPrem)
    print("-----------------------------------------------------------")
    return totalPrem

def calcRegIncome(costPG, gasSold):
    totalReg = costPG * gasSold
    print("The total earned income earned from REGULAR gas is $", totalReg)
    print("-----------------------------------------------------------")
    return totalReg

def calcDiesIncome(costPG, gasSold):
    totalDeez = costPG * gasSold
    print("The total earned income earned from DIESEL gas is $", totalDeez)
    print("-----------------------------------------------------------")
    return totalDeez

def calcTotalSales(premium, regular, diesel):
    grossSale = premium + regular + diesel
    print("The total gross income from all comes out to $", grossSale)
    print("-----------------------------------------------------------")
    return grossSale
#use math module to make results not ..999.. off the screen
def calcTotalTaxes(sale):
    totalTax = sale * .075
    totalTax = math.ceil(totalTax)
    print("The total tax amount for the business this month comes out to $", totalTax)
    print("-----------------------------------------------------------")
    return totalTax

def calcBusinessIncome(sales, tax):
    totalIncome = sales - tax
    print("Our total business income for the month come out to $", totalIncome)
    print("-----------------------------------------------------------")
    return totalIncome

printIncomeReport()
