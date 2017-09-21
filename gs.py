#!/usr/bin/env python
# Script to demo the Gale-Shapley algorithm
# as in "Design of Algorithms", Kleinberg & Tardos
# Package HeapDict 1.0.0 needs to be installed
# Originally from Moodle
# Modified by: Elizabeth Gramzow, Yazeed Aldalbahi
# Date: 9/21/17

from __future__ import division 
import numpy as np
from heapdict import heapdict
import copy
import pprint

rank = dict()
rank['Abe']=('Abi','Eve','Cat','Ivy','Jan','Dee','Fay','Bea','Hope','Gay')
rank['Bob']=('Cat','Hope','Abi','Dee','Eve','Fay','Bea','Jan','Evy','Gay')
rank['Col']=('Hope','Eve','Abi','Dee','Bea','Fay','Ivy','Gay','Cat','Jan')
rank['Dan']=('Ivy','Fay','Dee','Gay','Hope','Eve','Jan','Bea','Cat','Abi')
rank['Ed']=('Jan','Dee','Bea','Cat','Fay','Eve','Abi','Ivy','Hope','Gay')
rank['Fred']=('Bea','Abi','Dee','Gay','Eve','Ivy','Cat','Jan','Hope','Fay')
rank['Gav']=('Gay','Eve','Ivy','Bea','Cat','Abi','Dee','Hope','Jan','Fay')
rank['Hal']=('Abi','Eve','Hope','Fay','Ivy','Cat','Jan','Bea','Gay','Dee')
rank['Ian']=('Hope','Cat','Dee','Gay','Bea','Abi','Fay','Ivy','Jan','Eve')
rank['Jon']=('Abi','Fay','Jan','Gay','Eve','Bea','Dee','Cat','Ivy','Hope')
rank['Abi']=('Bob','Fred','Jon','Gav','Ian','Abe','Dan','Ed','Col','Hal')
rank['Bea']=('Bob','Abe','Col','Fred','Gav','Dan','Ian','Ed','Jon','Hal')
rank['Cat']=('Fred','Bob','Ed','Gav','Hal','Col','Ian','Abe','Dan','Jon')
rank['Dee']=('Fred','Jon','Col','Abe','Ian','Hal','Gav','Dan','Bob','Ed')
rank['Eve']=('Jon','Hal','Fred','Dan','Abe','Gav','Col','Ed','Ian','Bob')
rank['Fay']=('Bob','Abe','Ed','Ian','Jon','Dan','Fred','Gav','Col','Hal')
rank['Gay']=('Jon','Gav','Hal','Fred','Bob','Abe','Col','Ed','Dan','Ian')
rank['Hope']=('Gav','Jon','Bob','Abe','Ian','Dan','Hal','Ed','Col','Fred')
rank['Ivy']=('Ian','Col','Hal','Gav','Fred','Bob','Abe','Ed','Jon','Dan')
rank['Jan']=('Ed','Hal','Gav','Abe','Bob','Jon','Col','Ian','Fred','Dan')
women = ['Abi','Bea','Cat','Dee','Eve','Fay','Gay','Hope','Ivy','Jan']
men = ['Abe','Bob','Col','Dan','Ed','Fred','Gav','Hal','Ian','Jon']

#print each person and their preferences
print '\nParticipants:'
print men
print women

print '\nPreferences:'
for person in rank.keys():
    print '{}: {}'.format(person, rank[person])
print '--------------------------------------------------\n'

N = len(rank)/2

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
    print '{} proposes to {}'.format(m,w)

    if w not in matchedW:                       # if w is free
        matchedM[m] = w                         # assign w to m
        matchedW[w] = m                         # assign m to w
        count[men.index(m)] += 1                # increment count of proposals
        print '{} accepts, since previously unmatched'.format(w)

    elif rank[w].index(m) < rank[w].index(matchedW[w]):   # if w prefers m to her fiancee m'
        m1 = matchedW[w]                                # w was matched with m1
        FreeMen[m1] = N - np.sum(count)          # put m' back in the PQ at the top
        FreeMen._min_heapify(0)
        matchedM[m] = w                         # assign w to m
        matchedW[w] = m                         # assign m to w
        count[men.index(m)] += 1                # increment count of proposals
        print '{} dumps {} and accepts {}'.format(w, m1, m)
    else:
	# m was rejected, get him back to the PQ at the top
        FreeMen[m] = N - np.sum(count)          
	
        FreeMen._min_heapify(0)
        count[men.index(m)] += 1                # increment count of proposals
        print '{} rejects since she prefers {}'.format(w, matchedW[w])
        
print '\nStable Matching:'
pprint.pprint(matchedM, width=1)

 


