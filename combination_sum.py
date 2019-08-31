# author : YANG CUI
"""
Given a set of candidate numbers (candidates) (without duplicates)
and a target number (target), find all unique combinations in candidates
where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of
times.
"""

def combination_sum_aux(inputList, target):
    # sort the list: O(nlogn)
    inputList.sort()
    resultList = []
    currentIndex = 0
    resultSeq = []
    combination_sum(inputList, target, currentIndex, resultSeq, resultList)
    return resultList

def combination_sum(inputList, target, currentIndex, resultSeq, resultList):
    for j in range(currentIndex, len(inputList)):
        # choose
        num = inputList[j]
        if num > target:
            return
        resultSeq.append(num)
        # explore
        if num < target:
            combination_sum(inputList, target - num, j, resultSeq, resultList)
        else:
            resultList.append(list(resultSeq))
        # unchoose
        resultSeq.pop()
    return
