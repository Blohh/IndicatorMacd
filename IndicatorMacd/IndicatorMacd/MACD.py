class MACD:
    """Class represents indicator MACD and has methods to calculate all its elements"""
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
        self.buy_sell_signal=[]
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



