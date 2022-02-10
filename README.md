# Information Retrieval Metrics and Plots Computation

A python script that computes common Information Retrieval's metrics and creates a Precision-Recall curve plot for a given set of results.

**Metrics computed by this script:**
- Set of Precision values for each query.
- Set of Recall values for each query.
- Average Precision (AvP) for each query.
- Mean Average Precision (MAP) for all queries.

**Plots:**
- Precision-Recall Curve for a single or multiple query (non-interpolated).



## Table of Contents 
1. [Installation Requirements](#installation)
2. [Usage Examples](#usage)
    1. [How to use?](#how-to)
    2. [Example 1: Single Query](#example1)
    3. [Example 2: Multiple Queries](#example2)
4. [Evaluation in Information Retrieval Briefly Explained](#explanation)
    1. [Precision and Recall](#precision-recall)
    2. [Average Precision](#ap)
    3. [Mean Average Precision](#map)
    4. [Precision-Recall Curves](#curves)
    5. [Practical Example](#practical-example)
    6. [Further Reading](#further-reading)

<a name="installation"/>

## Instalation Requirements 

To execute this script from the terminal you should have installed:

- [Python](https://www.python.org/downloads/).
- [Pip](https://pypi.org/project/pip/) that allows to install python's packages.
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

<a name="usage"/>

## Usage Examples 

<a name="how-to"/>

### How to use? 

From the terminal, execute the script passing two arguments:
1. Ordered set of relevant and non-relevant results.
2. Total number of relevant documents on the collection for the information need. 

So,
```
python computeMetrics.py *<orderedSet>* *<totalNumberRelevant>*
```

You can also use this script to evaluate more than one query:
```
python computeMetrics.py *<orderedSet1,orderedSet2,...,orderedSet7>* *<totalNumberRelevant1, totalNumberRelevant2, ..., totalNumberRelevant7>*
```

<a name="example1"/>

### Example 1: Single Query 

In order to compute the metrics for a single query, run on the terminal:

```
python computeMetrics.py RNRRRRNNNR 6
```

Again, the number '6' means that there are in total 6 documents in the collection that are relevant to the information need being evaluated.

The script prints as result:

```
SET: RNRRRRNNNR

PRECISION: [1.0, 0.5, 0.6666666666666666, 0.75, 0.8, 0.8333333333333334, 0.7142857142857143, 0.625, 0.5555555555555556, 0.6]

RECALL: [0.16666666666666666, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 1.0]

AVERAGE PRECISION: 0.7749999999999999

MAP: 0.7749999999999999
```

And creates the Precision-Recall curve plot:
![p-r curve for example 1](docs/example1.png)


<a name="example2"/>

### Example 2: Multiple Queries 

In order to compute the metrics for multiple queries, run on the terminal:

```
python3 computeMetrics.py RNRNNRNNRR,NRNNRNRNNN 6,6
```

The script prints as result:

```
SET: RNRNNRNNRR

PRECISION: [1.0, 0.5, 0.6666666666666666, 0.5, 0.4, 0.5, 0.42857142857142855, 0.375, 0.4444444444444444, 0.5]

RECALL: [0.16666666666666666, 0.16666666666666666, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.5, 0.5, 0.5, 0.6666666666666666, 0.8333333333333334]

AVERAGE PRECISION: 0.6222222222222221


SET: NRNNRNRNNN

PRECISION: [0.0, 0.5, 0.3333333333333333, 0.25, 0.4, 0.3333333333333333, 0.42857142857142855, 0.375, 0.3333333333333333, 0.3]

RECALL:[0.0, 0.16666666666666666, 0.16666666666666666, 0.16666666666666666, 0.3333333333333333, 0.3333333333333333, 0.5, 0.5, 0.5, 0.5]

AVERAGE PRECISION: 0.44285714285714284

MAP: 0.5325396825396824
```

And creates the Precision-Recall curve plot:
![p-r curve for example 2](docs/example2.png)


<a name="explanation"/>

## Evaluation in Information Retrieval Briefly Explained

A standard approach to evaluate a Information retrieval system uses the notion of relevant and non-relevant documents for a information need. 

The user performs a search in order to answer a information need. The results retrived by the system can be classified as relevant or non-relevant whether addresses the stated information need or not.

<a name="precision-recall"/>

### Precision and Recall

The most frequent metrics used in Information Retrieval evaluation are the concepts of Precision and Recall. 

Precision is the fraction of retrieved documents that are relevant.
```
Precision = #(relevant items retrieved) / #(total retrieved items)
```

Recall is the fraction of relevant documents that are retrieved. 
```
Recall = #(relevant items retrieved) / #(total relevant items in the collection)
```

<a name="avp"/>

### Average Precision 

Average Precision (AvP) provides a single-figure measure of quality across recall levels for a single query. It is the average of the precision value obtained after each relavant document is retrieved in the resuls lists.

<a name="map"/>

### Mean Average Precision

Mean Average Precision (MAP) is the mean of AvP values for a given set of queries. It is a good measure for the quality of a system.

<a name="curves"/>

### Precision-Recall Curves

A Precision-Recall curve plots the tradeoff between precision and recall for different threshold.

<a name="practical-example"/>

### Practical Example

A user wants to information on whether eating fruits can improve his immune system (**information need**).
The user search for [fruits improve immune system] (**query**).

Let's assume that the system returned 5 results.
From the first result to the left they were classified as - Relevant, Relevant, Non-Relevant, Relevant, Non-Relevant - to the user's information need. This can be translated into the set RRNRN.
Let's also assume that in the index collection there are in total 8 results relevant to this information need. 

```
Precision = (3 / 5) = 0.6
Recall = (3 / 8) = 0.375
```

We can compute the precision and recall value at each position of the 5 results.

| **Results** | R | R | N | R | N |
| --- | --- | --- | --- | --- | --- |
| **Recall** | 1/8 | 2/8 | 2/8 | 3/8 | 3/8 |
| **Precision** | 1/1 | 2/2 | 2/3 | 3/4 | 3/5 |

We can compute the average precision (AvP) using the values of precision for relevant documents. 

```
AvP = (1/1 + 2/2 + 3/4) / 3 = 0.91 
```

Let's assume that the user did another search and for other a different information need, the system displayed an average precision of 0.82. 

We can compute the system's Mean Average Precision (MAP) for both information needs as:
```
MAP = (0.91 + 0.82) / 2 = 0.865
```

<a name="further-reading"/>

### Further Reading
```
Manning, C., Raghavan, P., Schutze, H. (2009). An Introduction to Informational Retrieval. Cambridge University Press.
```