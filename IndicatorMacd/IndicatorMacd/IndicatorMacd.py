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
    def createCurrencyDiagram(self):
        plt.figure(1)
        plt.plot(date[35::], course[35::], label="course", color="green")
        plt.legend()
        plt.grid(True)
        plt.xlabel("Date")
        plt.ylabel("Course")
        plt.title(self.name+" course")
    def showCurrencyDiagram(self):
        self.createCurrencyDiagram()
        plt.show()


class MACD:
    macd=[]
    signal=[]
    buy_sell_signal=[]
    def __init__(self, course, date):
        self.calculateMACD(course)
        self.calculateSIGNAL()
        self.calculateBuySellSignals()
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
    def calculateBuySellSignals(self):
        tmp_macd=self.macd[35::]
        for i in range(1, len(tmp_macd)):
            if tmp_macd[i-1]<self.signal[i-1] and tmp_macd[i] > self.signal[i]:
                self.buy_sell_signal.append("buy")
            elif tmp_macd[i-1]>self.signal[i-1] and tmp_macd[i] < self.signal[i]:
                self.buy_sell_signal.append("sell")
            else:
                self.buy_sell_signal.append("noaction")

    def createMACDDiagram(self):
        plt.figure(2)
        plt.plot(date[35::], self.macd[35::], label="macd", color="blue")
        plt.plot(date[35::], self.signal, label="signal", color="red")
        plt.legend()
        plt.grid(True)
        plt.xlabel("Date")
        plt.title("MACD")
    def createBuySellDiagram(self):
        plt.figure(3)
        plt.plot(date[35:999], self.buy_sell_signal, label="buy_sell_signal", color="yellow")
        plt.legend()
        plt.grid(True)
        plt.xlabel("Date")
        plt.ylabel("Buy-sell signals")
        plt.title("Buy-sell signals")
    def showMACDDiagram(self):
        self.createMACDDiagram()
        plt.show()
    def showMACDDiagramWithBuySell(self):
        self.createMACDDiagram()
        self.createBuySellDiagram()
        plt.show()

    

    
    
    



if __name__ == '__main__':
    currency = Currency("jen_japonski")
    date, course=currency.createData()
    macd=MACD(course, date)
    currency.createCurrencyDiagram()
    macd.showMACDDiagram()
    
