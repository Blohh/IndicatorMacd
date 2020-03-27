import pandas as pd
class Currency:
    """Class represents currency course"""
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
        self.course=list(data["price(USD)"])
        self.date=list(data["date"])
        return self.date, self.course
    def getCourse(self):
        return self.course
    def getDate(self):
        return self.date

