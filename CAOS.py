import csv
from ARA import *
from SA import *
from functions import *
from DM import *




class Company:
    def __init__(self, name, activity):
        self.name = name
        self.activity = activity
    
class StockAnalysis:
    def __init__(self, market_value, inner_value, outstanding_shares):
        self.market_value = market_value
        self.inner_value = inner_value
        self.outstanding_shares = outstanding_shares

    def difference(self):
        return self.market_value - self.inner_value


class AnnualReportAnalysis:
    def __init__(self):
        self.ag = ARA.calculateAg(operating_profit, financial_income, ga)
        self.og = ARA.calculateOg(operating_profit, financial_income, revenue)
        self.aoh = ARA.calculateAoh(revenue, ga)
        self.gr = ARA.calculateGr(financial_costs, gf)
        self.ekf = ARA.calculateEkf(result_before_tax, ge)
        self.gearing = ARA.calculateGearing(ge, ga)
        self.sg = ARA.calculateSg(equity, assets)
        self.market_price = market_price
        #self.lg = ARA.calculateLg(1,1)
        
        self.indicators = [self.market_price, self.ag, self.og, self.aoh, self.gr, self.ekf, self.gearing, self.sg]

class Modelling:
    def __init__(self):
        self.ag = ARA.calculateAg(operating_profit, financial_income, ga)
        self.og = ARA.calculateOg(operating_profit, financial_income, revenue)
        self.aoh = ARA.calculateAoh(revenue, ga)
        self.gr = ARA.calculateGr(financial_costs, gf)
        self.ekf = ARA.calculateEkf(result_before_tax, ge)
        self.gearing = ARA.calculateGearing(ge, ga)
        self.sg = ARA.calculateSg(equity, assets)
        #self.lg = ARA.calculateLg(1,1)
        self.eps = SA.EPS(taxed_result,shares)
        self.absPE = SA.absolutePE(market_price,SA.EPS(taxed_result,shares))
        self.market_price = market_price
        self.intrinsicVal = SA.intrinsicValue(equity,shares)
        self.delta = SA.Delta(SA.intrinsicValue(equity,shares),market_price)
        self.indicators = [self.ag, self.og, self.aoh, self.gr, self.ekf, self.gearing, self.sg, self.eps, self.absPE, self.market_price, self.intrinsicVal, self.delta]        

# Annual report element
"""
def flush():
    file = open("data.csv", "w")
    reader = csv.reader(file)
    for item in reader:
        writerow = ""
    file.close()
"""

t = Modelling()
print("Afkastningsgrad:                 "+str(t.ag))
print("Overskudsgrad:                   "+str(t.og))
print("Aktivernes omsætningshastighed:  "+str(t.aoh))
print("Gældsrente:                      "+str(t.gr))
print("Egenkapitalens forrentning:      "+str(t.ekf))
print("Gearing:                         "+str(t.gearing))
print("Soliditetsgrad:                  "+str(t.sg))
#print("Likviditetsgrad:                "+str(t.lg))
print("Earnings pr. share:              "+str(t.eps))
print("Absolute P/E:                    "+str(t.absPE))
print("Market price:                    "+str(t.market_price))
print("Intrinsic value:                 "+str(t.intrinsicVal))
print("Price delta:                     "+str(t.delta))
file = open("data.csv", "a")
writer = csv.writer(file)
writer.writerow(t.indicators)
file.close()



# Formatting syntax: "Hi I am {}".format("Kasper")
