# author: YANG CUI
"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations
***DFS approach***
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
        if j == currentIndex or inputList[j] != inputList[j-1]:
            # choose
            num = inputList[j]
            if num > target:
                return
            resultSeq.append(num)
            # explore
            if num < target:
                combination_sum(inputList, target - num, j + 1, resultSeq, resultList)
            else:
                # if resultSeq not in resultList:
                    resultList.append(list(resultSeq))
            # unchoose
            resultSeq.pop()
    return

# print(combination_sum_aux([10,1,2,7,6,1,5], 8))

