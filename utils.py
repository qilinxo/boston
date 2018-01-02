import numpy as np
from sklearn import datasets 
import pandas as pd

def loadData(fileTitle):
    file = open(fileTitle)
    tempDataSet = file.readlines()
    file.close()
    file = open('./boston2.txt', 'w')
    tempLine = ''
    i = 0
    dataSet = []
    condition = lambda t: t != ''
    for line in tempDataSet:
        if i%2 == 1:
            tempLine = tempLine + line 
            tempLine = tempLine.replace('\n', '')
            #file.write('\n'+tempLine)
            tempList = tempLine.split(" ")
            tempList = list(filter(condition, tempList))
            for i in range(len(tempList)):
                tempList[i] = float(tempList[i])
            dataSet.append(tempList)
        if i%2 == 0:
            tempLine = line
        i += 1
    #file.close()
    return dataSet

def loadNpData(fileTitle):
    dataMatrix = np.loadtxt(fileTitle)
    return dataMatrix

def loadBySklearn():
    boston = datasets.load_boston()
    return boston['data'], boston['target'], boston['feature_names']

if __name__ == "__main__":
    dataSet = loadData('./boston.txt')
    #dataSet = loadNpData('./boston2.txt')
    dataSet = pd.DataFrame(dataSet, columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS',
         'RAD', 'TAX', 'PRTATIO', 'B', 'LSTAT', 'MEDV'] )
    #print(x, y, features)
    #print(features.dtype)

    print(dataSet)
    #print(np.shape(np.mat(dataSet)))