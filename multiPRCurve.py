from sklearn.metrics import PrecisionRecallDisplay
import statistics
import matplotlib.pyplot as plt
import sys

# Computes Precision, Recall and Average Precision.
# For that, it is necessary the ordered set of relevant and non-relevant results
# and the total number of relevant documents in the colection.
def computeAvP(set, numTotalRelevant, precision, recall, averagePrecision):
    characters = list(set)
    totalRelevantAlreadyFound = 0

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
    return averagePrecision


# Plots Precision-Recall curves for multiple queries.
def plotMultiplePrecisionRecallCurve(precision, recall):
    _, ax = plt.subplots(figsize=(7, 8))
    colors = ["navy", "darkorange", "teal", "red", "bisque", "olive", "lavender"]

    for idx, prec in enumerate(precision):
        disp = PrecisionRecallDisplay(precision[idx], recall[idx])
        label = "Precision-recall for query #" + str(idx+1)
        disp.plot(ax=ax, name=label, color=colors[idx])
    
    plt.legend(loc='lower right')
    plt.savefig('precisionRecall.pdf')


# Computes Mean Average Precision.
def computeMAP(avpSet):
    MAP = statistics.mean(avpSet)
    print("\nMAP")
    print(MAP)



# Main.

results = sys.argv[1].split(",")
numTotalRelevant = sys.argv[2].split(",")

precisionSet = []
recallSet = []
avpSet = []

# For each set of query's results.
for idx, set in enumerate(results):
    precision = []
    recall = []
    averagePrecision = 0

    avpSet.append(computeAvP(results[idx], int(numTotalRelevant[idx]), precision, recall, averagePrecision))
    precisionSet.append(precision)
    recallSet.append(recall)


print(avpSet)
computeMAP(avpSet)
plotMultiplePrecisionRecallCurve(precisionSet, recallSet)

