class Simulation:
    """ Class which conduct simulation of buying/selling currency depending of MACD buy/sell signals"""
    def simulate(self, course, buy_sell_signal, starting_cash):
        cash=starting_cash
        deposited_cash=0
        tmp_course=course[35::]
        for i in range(len(buy_sell_signal)):
            if(buy_sell_signal[i]=="buy"):
                print("Deposited "+str(cash)+" $")
                deposited_cash=round(cash/tmp_course[i], 2)
                cash=0
            elif(buy_sell_signal[i]=="sell"):
                cash+=round(deposited_cash*tmp_course[i], 2)
                deposited_cash=0
                print("Got "+str(cash)+" $")
        print("\nAt the end you have "+str(cash+round(deposited_cash*course[999], 2))+" $")
        print("You begin with "+str(starting_cash)+" $")