import pandas as pd
import numpy as np

class Currency:
    name = ""
    course=[]
    date=[]
    def __init__(self, name):
        self.name=name
    def getName(self):
        return name
    def createData(self):
        filename="./data/"+str(self.name)+".csv"
        data=pd.read_csv(str(filename),delimiter=",")
        course=data["Course"]
        date=data["Date"]
        return date, course

class MACD:
    macd=[]
    signal=[]
    def __init__(self, course, date):
        calculateMACD(course)
        calculateSIGNAL(course)
    def calculateMACD(course):
        for i in range(len(course)):
            if i>=26:
                ema12=calculateEMA(course, i, 12)
                ema26=calculateEMA(course, i, 26)
                macd.append(ema12-ema26)
            else:
                macd.append(0.0)



if __name__ == '__main__':
    currency = Currency("jen_japonski")
    date, course=currency.createData()
    