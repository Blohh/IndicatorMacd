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
        return self.name
    def createData(self):
        filename="./data/"+str(self.name)+".csv"
        data=pd.read_csv(str(filename),delimiter=",")
        self.course=list(data["Course"])
        self.date=list(data["Date"])
        self.course.reverse()
        self.date.reverse()
        return self.date, self.course
    def getCourse(self):
        return self.course
    def getDate(self):
        return self.date


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
    def getMACD(self):
        return self.macd
    def getSignal(self):
        return self.signal
    def getBuySellSignal(self):
        return self.buy_sell_signal

  

    
class Diagram:
    def prepareMACDDiagram(self, date, macd, signal):
        plt.plot(date[35::], macd[35::], label="macd", color="blue")
        plt.plot(date[35::], signal, label="signal", color="red")
        plt.legend()
        plt.grid(True)
        plt.xlabel("Date")
        plt.title("MACD")
    def prepareCurrencyDiagram(self, date, currency, name):
        plt.plot(date[35::], course[35::], label="course", color="green")
        plt.legend()
        plt.grid(True)
        plt.xlabel("Date")
        plt.ylabel("Course")
        plt.title(name+" course")
    def prepareBuySellDiagram(self, date, buy_sell_signal ):
        plt.plot(date[35:999], self.buy_sell_signal, label="buy_sell_signal", color="yellow")
        plt.legend()
        plt.grid(True)
        plt.xlabel("Date")
        plt.ylabel("Buy-sell signals")
        plt.title("Buy-sell signals")
    def showMACDDiagram(self, date, macd, signal):
        plt.figure(1)
        self.prepareMACDDiagram(date, macd, signal)
        plt.show()
    def showCurrencyDiagram(self, date, currency, coursename):
        plt.figure(1)
        self.prepareCurrencyDiagram(date, currency, coursename)
        plt.show()
    def showMACDAndCurrency(self, date, macd, signal, currency, coursename):
        plt.figure(1)
        self.prepareCurrencyDiagram(date, currency, coursename)
        plt.figure(2)
        self.prepareMACDDiagram(date, macd, signal)
        plt.show()
    def showEverything(self, date, macd, signal, currency, buy_sell_signal, coursename):
        plt.figure(1)
        self.prepareCurrencyDiagram(date, currency, coursename)
        plt.figure(2)
        self.prepareMACDDiagram(date, macd, signal)
        plt.figure(3)
        self.prepareBuySellDiagram(date, buy_sell_signal)
        plt.show()
    
    
class Simulation:
    def simulate(self, date, course, buy_sell_signal, starting_cash):
        cash=starting_cash
        deposited_cash=0
        tmp_date=date[35::]
        for i in range(len(buy_sell_signal)):
            if(buy_sell_signal[i]=="buy"):
                print("Deposited "+str(cash)+" $")
                deposited_cash=round(cash/course[i], 2)
                cash=0
            elif(buy_sell_signal[i]=="sell"):
                cash+=round(deposited_cash*course[i], 2)
                deposited_cash=0
                print("Got "+str(cash)+" $")
        print("\nAt the end you have "+str(cash+round(deposited_cash*course[999], 2))+" $")
        print("You begin with "+str(starting_cash)+" $")




if __name__ == '__main__':
    currency = Currency("jen_japonski")
    date, course=currency.createData()
    macd=MACD(course, date)
    Diagram.showMACDAndCurrency(Diagram(), currency.getDate(), macd.getMACD(), macd.getSignal(), currency.getCourse(), currency.getName())
    Simulation.simulate(Simulation(), currency.getDate(), currency.getCourse(), macd.getBuySellSignal(), 1000)
    
