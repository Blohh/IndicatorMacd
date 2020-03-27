from Currency import Currency
from MACD import MACD
from Diagram import Diagram
from Simulation import Simulation


if __name__ == '__main__':
    currency = Currency("bitcoin")
    date, course=currency.createData()
    macd=MACD(course, date)
    Diagram.showMACDAndCurrency(Diagram(), currency.getDate(), macd.getMACD(), macd.getSignal(), currency.getCourse(), currency.getName())
    Diagram.showDiagramFromXToY(Diagram(), currency.getDate(), macd.getMACD(), macd.getSignal(), currency.getCourse(), currency.getName(), 0, 100)
    Simulation.simulate(Simulation(), currency.getCourse(), macd.getBuySellSignal(), 1000)
  
   

    
