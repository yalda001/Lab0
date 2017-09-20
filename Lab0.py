#!/usr/bin/env python
# Script to demo the Gale-Shapley algorithm
# as in "Design of Algorithms", Kleinberg & Tardos
# Package HeapDict 1.0.0 needs to be installed

from __future__ import division 
import numpy as np
from heapdict import heapdict
import copy
import pprint

FILE = 'gs_data_ch1'

# Execute file statements defining a dictionary with the rankings
execfile(FILE)
# Echo print
print '
\n
Rank data read from file {}
\n
'
.format(FILE)
pprint.pprint(rank)      # A dictionary with preferences of each person (men and women)
print '--------------------------------------------------
\n
'

N = len(rank)/
2

# Define a priority queue to keep the free men
FreeMen = heapdict()
for i in range(len(men)):
    FreeMen[men[i]] = i + N # priorities are offset by N to accomodate later insertions at the front

# Define dictionaries for matching: {m1:w1, m2:w2, ..., m_n:w_n} {w1:m1 ...}
matchedM = dict()
matchedW = dict()
count = np.zeros(N)     # Number of proposals of each man

# While some man is free and hasn't proposed to every woman
while FreeMen.__len__() != 0 and count[men.index(FreeMen.peekitem()[0])] < N:
    m = FreeMen.popitem()[0]                    # choose such a man m
    w = rank[m][int(count[men.index(m)])]            # 1st woman to which he hasn't yet proposed
    print '{} proposes to {}'
.format(m,w)

    if w not in matchedW:                       # if w is free
        matchedM[m] = w                         # assign w to m
        matchedW[w] = m                         # assign m to w
        count[men.index(m)] += 1                # increment count of proposals
        print '{} accepts, since previously unmatched'
.format(w)

    elif rank[w].index(m) < rank[w].index(matchedW[w]):   # if w prefers m to her fiancee m'
        m1 = matchedW[w]                                # w was matched with m1
        FreeMen[m1] = N - np.sum(count)          # put m' back in the PQ at the top
        FreeMen._min_heapify(0)
        matchedM[m] = w                         # assign w to m
        matchedW[w] = m                         # assign m to w
        count[men.index(m)] += 1                # increment count of proposals
        print '{} dumps {} and accepts {}'
.format(w, m1, m)
    else:
        FreeMen[m] = N - np.sum(count)          # m was rejected, get him back to the PQ at the top
        FreeMen._min_heapify(0)
        count[men.index(m)] += 1                # increment count of proposals
        print '{} rejects since she prefers {}'
.format(w, matchedW[w])
        
print '
\n
Stable Matching:'
pprint.pprint(matchedM, width=
1)

 
rank = dict()
rank['Victor']=('Bertha','Amy','Diane','Erika','Clare')
rank['Wyatt']=('Diane','Bertha','Amy','Clare','Diane')
rank['Xavier']=('Bertha','Erika','Clare','Diane','Amy')
rank['Yancey']=('Amy','Diane','Clare','Bertha','Erika')
rank['Zeus']=('Bertha','Diane','Amy','Diane','Clare')
rank['Amy']=('Zeus','Victor','Wyatt','Yancey','Xavier')
rank['Bertha']=('Xavier','Wyatt','Yancey','Victor','Zeus')
rank['Clare']=('Wyatt','Xavier','Yancey','Zeus','Victor')
rank['Diane']=('Victor','Zeus','Yancey','Xavier','Wyatt')
rank['Erika']=('Yancey','Wyatt','Zeus','Xavier','Victor')
women = ['Amy','Bertha','Clare','Diane','Erika']
men = ['Victor','Wyatt','Xavier','Yancey','Zeus']

