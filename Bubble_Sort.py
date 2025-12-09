Number_Sort = [16,857,257,856,25,287,645,8647,345,816,73,54,15,87,65,87,94,984,561984,156874,156984516,516,456]

for y in range(len(Number_Sort)-1):
    for i in range(len(Number_Sort)-1-y):
        if Number_Sort[i] > Number_Sort[i+1]:
            temp = Number_Sort[i]
            Number_Sort[i] = Number_Sort[i+1]
            Number_Sort[i+1] = temp
        
    print(Number_Sort)
