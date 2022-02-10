# Information Retrieval Metrics and Plots Computation

A python script that computes common Information Retrieval's metrics and creates a Precision-Recall curve plot for a given set of results and a given set of the total number of relevant documents in the collection for each information need.

**Metrics computed by this script:**
- Set of Precision values.
- Set of Recall values.
- Average Precision (AvP).
- Mean Average Precision (MAP).

**Plots:**
- Precision-Recall Curve for a single or multiple query.


## Installation Requirements

The script can be executed from a terminal with Python and the next packages installed.

- [Python](https://www.python.org/downloads/).
- [Pip] that allows to install Python's packages.
```
python -m pip install -U pip
```
- [scikit-learn](https://scikit-learn.org/stable/install.html) package.
```
pip install -U scikit-learn
```
- [matplotlib](https://matplotlib.org/stable/users/installing/index.html) package. 
```
python -m pip install -U matplotlib
```

## Usage

### How to use the script?

From the terminal, call the script's name passing as arguments:
1. Ordered set of relevant and non-relevant documents.
2. Total number of relevant documents on the collection for the information need. 

So,
```
python computeMetrics.py _<orderedSet>_ _<totalNumberRelevant>_
```

You can also use this script with more than one query:
```
python computeMetrics.py _<orderedSet1,orderedSet2,...,orderedSet7>_ _<totalNumberRelevant1, totalNumberRelevant2, ..., totalNumberRelevant7>_
```

### Example 1: Single Query

In order to compute the metrics for a single queries, we can run the next terminal command:

```
python computeMetrics.py RNRRRRNNNR 6
```

The script is going to print on the console the next log:

```
SET:
RNRRRRNNNR

PRECISION:
[1.0, 0.5, 0.6666666666666666, 0.75, 0.8, 0.8333333333333334, 0.7142857142857143, 0.625, 0.5555555555555556, 0.6]

RECALL:
[0.16666666666666666, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 1.0]

AVERAGE PRECISION: 
0.7749999999999999

MAP:
0.7749999999999999
```

And will create the next plot:
![p-r curve for example1](docs/example1.png)


### Example 1: Multiple Queries

In order to compute the metrics for multiple queries, we can run the next terminal command:

```
python computeMetrics.py RNRRRRNNNR 6
```

The script is going to print on the console the next log:

```
SET:
RNRRRRNNNR

PRECISION:
[1.0, 0.5, 0.6666666666666666, 0.75, 0.8, 0.8333333333333334, 0.7142857142857143, 0.625, 0.5555555555555556, 0.6]

RECALL:
[0.16666666666666666, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 1.0]

AVERAGE PRECISION: 
0.7749999999999999

MAP:
0.7749999999999999
```

And will create the next plot:
![p-r curve for example1](docs/example2.png)