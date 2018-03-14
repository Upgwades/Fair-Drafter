"""
Author: Will Irwin
Last Modified: 10/14/2017
Inputs:
    text inputs provided on screen
Outputs:
    a fair draft based on the given parameters
Instructions to run w/ no install:
    goto https://repl.it/languages/python
    paste this code into the text box on the left
    run and input the requested information
"""
import os
import random
import numpy as np

def input():
        playersString = raw_input("Enter player names separated with commans and no spaces: ")
        players = [x.strip() for x in playersString.split(',')]
        rounds = int(raw_input('Enter the number of rounds: '))
        iterations = int(raw_input('Enter the number of times to run the program: '))
        weight = raw_input('Weighted rounds (getting the pick in the first pick in an early round is worth more than in later rounds)? (y/n): ')
        if weight == "y":
            weight = True
        elif weight == "n":
            weight = False
        return players, rounds, weight, iterations

def draftPicker(players, rounds, weight):
        w, h = len(players), rounds
        weights = list(reversed(range(1, rounds+1)))
        tolerance = 0.0

        fair = False

        while not fair:

            orderMatrix = []
            weightedMatrix = []
            averages = []

            for x in range(0,rounds):
                orderMatrix.append(random.sample(range(1, len(players)+1), len(players)))

            orderMatrix = zip(*orderMatrix)

            if weight:
                for x in range(0,len(players)):
                    weightedMatrix.append([a*b for a,b in zip(weights,orderMatrix[x])])

                for values in weightedMatrix:
                    averages.append(float(sum(values)/float(len(values))))
            else:
                for values in orderMatrix:
                    averages.append(float(sum(values)/float(len(values))))

            overallAverage = float(sum(averages)/float(len(averages)))
            q51, q49 = np.percentile(averages, [51 ,49])
            fair = (averages >= (q49-tolerance)).all() and (averages <= (q51+tolerance)).all()
            tolerance = tolerance + .01
        return orderMatrix, averages, tolerance, overallAverage

def main():
    players, rounds, weight, iterations = input()
    tempOrderMatrix = []
    tempAverageMatrix = []
    tempToleranceMatrix = []
    tempOverallAverageMatrix = []

    for x in range(0,iterations):
        orderMatrix, averages, tolerance, overallAverage = draftPicker(players, rounds, weight)
        tempOrderMatrix.append(orderMatrix)
        tempAverageMatrix.append(averages)
        tempToleranceMatrix.append(tolerance)
        tempOverallAverageMatrix.append(overallAverage)
        print("crunching numb3rs...")

    minIndex = tempToleranceMatrix.index(min(tempToleranceMatrix))
    orderMatrix = tempOrderMatrix[minIndex]
    averages = tempAverageMatrix[minIndex]
    tolerance = tempToleranceMatrix[minIndex]
    overallAverage = tempOverallAverageMatrix[minIndex]

    print("\n")

    for x in range(0,len(players)):
        if weight == True:
            print(str(players[x]) + "'s drafting order is " + str(orderMatrix[x]) + " with an average weighted round pick of " + str(averages[x]))
        else:
            print(str(players[x]) + "'s drafting order is " + str(orderMatrix[x]) + " with an average round pick of " + str(averages[x]))
    print("\nAnd a fairness score of " + str(tolerance) + " (lower is better)")
main()
