import random

RandList = [random.randrange(100) for x in range(10)]
print(RandList)

def BubbleSort(OrignList):
    for j in range(len(OrignList)-1):
        for i in range(len(OrignList)-j-1):
            if OrignList[i] > OrignList[i+1]:
                temp = OrignList[i]
                OrignList[i] = OrignList[i+1]
                OrignList[i+1] = temp
    return OrignList

print(BubbleSort(RandList))
