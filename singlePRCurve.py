from sklearn.metrics import PrecisionRecallDisplay
import statistics
import matplotlib.pyplot as plt
import sys

# Computes Precision, Recall and Average Precision.
# For that, it is necessary the ordered set of relevant and non-relevant results
# and the total number of relevant documents in the colection.
def computeAvP(set, numTotalRelevant, precision, recall):
    characters = list(set)
    totalRelevantAlreadyFound = 0
    averagePrecision = 0

    # For each document result
    for idx, char in enumerate(characters):
        if (char.upper() == "R"): 
            totalRelevantAlreadyFound += 1
            averagePrecision = averagePrecision + totalRelevantAlreadyFound / (idx + 1)
        
        precision.append(totalRelevantAlreadyFound / (idx + 1))
        recall.append(totalRelevantAlreadyFound / numTotalRelevant)

    averagePrecision = averagePrecision / totalRelevantAlreadyFound

    print("\nSET: ")
    print(set)
    print("\nPRECISION: ")
    print(precision)
    print("\nRECALL:")
    print(recall)
    print("\nAverage Precision: ")
    print(averagePrecision)
    print("")


# Plots the Precision-Recall curve. 
def plotPrecisionRecallCurve(precision, recall):
    _, ax = plt.subplots(figsize=(7, 8))
    disp = PrecisionRecallDisplay(precision, recall)
    disp.plot(ax=ax, name=f"Precision-recall", color='navy')
    plt.savefig('precisionRecall.pdf')

# Main.

precision = []
recall = []

computeAvP(sys.argv[1], int(sys.argv[2]), precision, recall)
plotPrecisionRecallCurve(precision, recall)
