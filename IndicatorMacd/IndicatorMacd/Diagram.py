import matplotlib.pyplot as plt
class Diagram:
    """Class used to show diagrams of MACD, currency course and buy-sell signals """
    def prepareMACDDiagram(self, date, macd, signal, date_from=0, date_to=965):
        if date_from==0 and date_to==965:
            ticks=date[200:1000:200]
        else:
            ticks=date[date_from+35+int(date_to/5):date_to+35:int(date_to/5)]
        plt.plot(date[35+date_from:35+date_to], macd[35+date_from:date_to+35], label="macd", color="blue")
        plt.plot(date[35+date_from:35+date_to], signal[date_from:date_to], label="signal", color="red")
        plt.legend()
        plt.grid(True)
        plt.xlabel("Date")
        plt.title("MACD")
        plt.xticks(ticks)
    def prepareCurrencyDiagram(self, date, course, name, date_from=0, date_to=965):
        if date_from==0 and date_to==965:
            ticks=date[200:1000:200]
        else:
            ticks=date[date_from+35+int(date_to/5):date_to+35:int(date_to/5)]
        plt.plot(date[35+date_from:date_to+35], course[35+date_from:date_to+35], label="course", color="green")
        plt.legend()
        plt.grid(True)
        plt.xlabel("Date")
        plt.ylabel("Course")
        plt.title(name+" course")
        plt.xticks(ticks)
    def prepareBuySellDiagram(self, date, buy_sell_signal):
        ticks=date[200:1000:200]
        plt.plot(date[35:999], self.buy_sell_signal, label="buy_sell_signal", color="yellow")
        plt.legend()
        plt.grid(True)
        plt.xlabel("Date")
        plt.ylabel("Buy-sell signals")
        plt.title("Buy-sell signals")
        plt.xticks(ticks)
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
    def showDiagramFromXToY(self, date, macd, signal, currency, coursename, date_from, date_to):
        plt.figure(1)
        self.prepareCurrencyDiagram(date, currency, coursename, date_from, date_to)
        plt.figure(2)
        self.prepareMACDDiagram(date, macd, signal, date_from, date_to)
        plt.show()
    def showEverything(self, date, macd, signal, currency, buy_sell_signal, coursename):
        plt.figure(1)
        self.prepareCurrencyDiagram(date, currency, coursename)
        plt.figure(2)
        self.prepareMACDDiagram(date, macd, signal)
        plt.figure(3)
        self.prepareBuySellDiagram(date, buy_sell_signal)
        plt.show()
    