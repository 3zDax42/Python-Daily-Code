import random

RandList = [random.randrange(100) for x in range(50)]
print(RandList)

def InsertionSort(OrignList):
    for i in range(1, len(OrignList)):
        Key = OrignList[i]
        KeyN = i - 1

        while KeyN >=0 and Key < OrignList[KeyN]:
            OrignList[KeyN + 1] = OrignList[KeyN]
            KeyN -= 1
        OrignList[KeyN + 1] = Key
    return OrignList

print(InsertionSort(RandList))
