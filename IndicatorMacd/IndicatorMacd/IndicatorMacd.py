import pandas as pd
import numpy as np
import jupyter
import matplotlib.pyplot as plt

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
        self.calculateMACD(course)
        self.calculateSIGNAL()
        self.showMACDDiagram()
    def calculateMACD(self, course):
        for i in range(len(course)):
            if i>=26:
                ema12=self.calculateEMA(course, i, 12)
                ema26=self.calculateEMA(course, i, 26)
                self.macd.append(ema12-ema26)
            else:
                self.macd.append(0.0)
    def calculateEMA(self, course, x0, N):
            alpha=2/(N+1)
            counter=course[x0]
            denominator=1
            tmp=1-alpha
            for i in range(x0, x0-N-1, -1):
                counter+=course[i]*tmp
                denominator+=tmp
                tmp*=tmp
            return (counter/denominator)
    def calculateSIGNAL(self):
        for i in range(35, len(self.macd)):
            self.signal.append(self.calculateEMA(self.macd, i, 9))
    def showMACDDiagram(self):
        plt.plot(date[35::], self.macd[35::], label="macd", color="blue")
        plt.plot(date[35::], self.signal, label="signal", color="red")
        plt.legend()
        plt.grid(True)
        plt.xlabel("Date")
        plt.title("MACD")
        plt.show()

    

    
    
    



if __name__ == '__main__':
    currency = Currency("jen_japonski")
    date, course=currency.createData()
    macd=MACD(course, date)
    
