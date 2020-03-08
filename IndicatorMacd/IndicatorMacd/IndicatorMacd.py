import pandas as pd
import numpy as np

class Currency:
    __name = ""
    course=[]
    date=[]
    def __init__(self, name):
        self.__name=name
    def getName(self):
        return __name
    def createData(self):
        filename="./data/"+str(self.__name)+".csv"
        data=pd.read_csv(str(filename),delimiter=",")
        course=data["Course"]
        date=data["Date"]
        return date, course



if __name__ == '__main__':
    currency = Currency("jen_japonski")
    date, course=currency.createData()
    