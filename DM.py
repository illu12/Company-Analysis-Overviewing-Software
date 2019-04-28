import json
from functions import *
from urllib import request
from dictor import dictor
#dictor(DATA, TARGET)

"""
# Proces:
# Dataindsamlingen eksekveres i segmenter.
# Selve data indhentes via. json og laves om til et Python dictionary,
# derefter opstilles en 'list' til hver serie af data. Sidst kaldes funktioner der filtrerer data
# fra 'dictionary'.
#
# Denne proces sker ved hver json objekt, f.eks. ved resultatopgørelse og balancen.
#
# Resultatopgørelse:
#     url: https://financialmodelingprep.com/api/financials/income-statement/AAPL?datatype=json
# Balance:
#     url: https://financialmodelingprep.com/api/financials/balance-sheet-statement/AAPL?datatype=json
# 
"""



##### First code segment for the financial statement #####
url = "https://financialmodelingprep.com/api/financials/income-statement/AAPL?datatype=json"
r = request.urlopen(url)
dataset = json.loads(r.read())
print(dataset)
for i in dataset["AAPL"].keys():
    print(i)
print("\n")

# Income statement / resultatopgørelse
revenue = [] #omsætning
costOfRevenue = [] #vareforbrug
grossProfit = [] #bruttofortjeneste
researchAndDevelopment = [] 
salesAndAdministrative = [] #salgs og administrationsomkostninger
operatingIncome = [] #resultat af primær drift
interestExpenses = [] #finansielle omkostninger
otherIncome = [] #finansielle indtægter
incomeBeforeTaxes = [] #årets resultat før skat
provisionForIncomeTaxes = [] #Skat
netIncome = [] #årets resultat efter skat

def getRevenue(company):
    revenue.append(dictor(dataset,""+company+".Revenue.2014-09"))
    print("Revenue 2014: "+revenue[0])
    revenue.append(dictor(dataset,""+company+".Revenue.2015-09"))
    print("Revenue 2015: "+revenue[1])
    revenue.append(dictor(dataset,""+company+".Revenue.2016-09"))
    print("Revenue 2016: "+revenue[2])
    revenue.append(dictor(dataset,""+company+".Revenue.2017-09"))
    print("Revenue 2017: "+revenue[3])
    revenue.append(dictor(dataset,""+company+".Revenue.2018-09"))
    print("Revenue 2018: "+revenue[4])
    revenue.append(dictor(dataset,""+company+".Revenue.TTM"))
    print("Revenue 2019/TTM: "+revenue[5])
    print("\n")

def getCostOfRevenue(company):
    costOfRevenue.append(dictor(dataset,""+company+".Cost of revenue.2014-09"))
    print("Cost of revenue 2014: "+costOfRevenue[0])
    costOfRevenue.append(dictor(dataset,""+company+".Cost of revenue.2015-09"))
    print("Cost of revenue 2015: "+costOfRevenue[1])
    costOfRevenue.append(dictor(dataset,""+company+".Cost of revenue.2016-09"))
    print("Cost of revenue 2016: "+costOfRevenue[2])
    costOfRevenue.append(dictor(dataset,""+company+".Cost of revenue.2017-09"))
    print("Cost of revenue 2017: "+costOfRevenue[3])
    costOfRevenue.append(dictor(dataset,""+company+".Cost of revenue.2018-09"))
    print("Cost of revenue 2018: "+costOfRevenue[4])
    costOfRevenue.append(dictor(dataset,""+company+".Cost of revenue.TTM"))
    print("Cost of revenue 2019/TTM: "+costOfRevenue[5])
    print("\n")
    
def getGrossProfit(company):
    grossProfit.append(int(revenue[0])-int(costOfRevenue[0]))
    print("Gross profit 2014:"+str(grossProfit[0]))
    grossProfit.append(int(revenue[1])-int(costOfRevenue[1]))
    print("Gross profit 2015:"+str(grossProfit[1]))
    grossProfit.append(int(revenue[2])-int(costOfRevenue[2]))
    print("Gross profit 2016:"+str(grossProfit[2]))
    grossProfit.append(int(revenue[3])-int(costOfRevenue[3]))
    print("Gross profit 2017:"+str(grossProfit[3]))
    grossProfit.append(int(revenue[4])-int(costOfRevenue[4]))
    print("Gross profit 2018:"+str(grossProfit[4]))
    grossProfit.append(int(revenue[5])-int(costOfRevenue[5]))
    print("Gross profit 2019/TTM:"+str(grossProfit[5]))
    print("\n")
    
def getResearchAndDevelopment(company):
    researchAndDevelopment.append(dictor(dataset,""+company+".Research and development.2014-09"))
    print("R&D costs 2014: "+researchAndDevelopment[0])
    researchAndDevelopment.append(dictor(dataset,""+company+".Research and development.2015-09"))
    print("R&D costs 2015: "+researchAndDevelopment[1])
    researchAndDevelopment.append(dictor(dataset,""+company+".Research and development.2016-09"))
    print("R&D costs 2016: "+researchAndDevelopment[2])
    researchAndDevelopment.append(dictor(dataset,""+company+".Research and development.2017-09"))
    print("R&D costs 2017: "+researchAndDevelopment[3])
    researchAndDevelopment.append(dictor(dataset,""+company+".Research and development.2018-09"))
    print("R&D costs 2018: "+researchAndDevelopment[4])
    researchAndDevelopment.append(dictor(dataset,""+company+".Research and development.TTM"))
    print("R&D costs 2019/TTM: "+researchAndDevelopment[5])
    print("\n")

def getSalesAndAdministrative(company):
    salesAndAdministrative.append(dictor(dataset,""+company+".Sales, General and administrative.2014-09"))
    print("Sales and administrative costs 2014: "+salesAndAdministrative[0])
    salesAndAdministrative.append(dictor(dataset,""+company+".Sales, General and administrative.2015-09"))
    print("Sales and administrative costs 2015: "+salesAndAdministrative[1])
    salesAndAdministrative.append(dictor(dataset,""+company+".Sales, General and administrative.2016-09"))
    print("Sales and administrative costs 2016: "+salesAndAdministrative[2])
    salesAndAdministrative.append(dictor(dataset,""+company+".Sales, General and administrative.2017-09"))
    print("Sales and administrative costs 2017: "+salesAndAdministrative[3])
    salesAndAdministrative.append(dictor(dataset,""+company+".Sales, General and administrative.2018-09"))
    print("Sales and administrative costs 2018: "+salesAndAdministrative[4])
    salesAndAdministrative.append(dictor(dataset,""+company+".Sales, General and administrative.TTM"))
    print("Sales and administrative costs 2019/TTM: "+salesAndAdministrative[5])
    print("\n")

def getOperatingIncome(company):
    operatingIncome.append(dictor(dataset,""+company+".Operating income.2014-09"))
    print("Operating income 2014: "+operatingIncome[0])
    operatingIncome.append(dictor(dataset,""+company+".Operating income.2015-09"))
    print("Operating income 2015: "+operatingIncome[1])
    operatingIncome.append(dictor(dataset,""+company+".Operating income.2016-09"))
    print("Operating income 2016: "+operatingIncome[2])
    operatingIncome.append(dictor(dataset,""+company+".Operating income.2017-09"))
    print("Operating income 2017: "+operatingIncome[3])
    operatingIncome.append(dictor(dataset,""+company+".Operating income.2018-09"))
    print("Operating income 2018: "+operatingIncome[4])
    operatingIncome.append(dictor(dataset,""+company+".Operating income.TTM"))
    print("Operating income 2019/TTM: "+operatingIncome[5])
    print("\n")

def getInterestExpenses(company):
    interestExpenses.append(dictor(dataset,""+company+".Interest Expense.2014-09"))
    print("Interest expenses 2014: "+interestExpenses[0])
    interestExpenses.append(dictor(dataset,""+company+".Interest Expense.2015-09"))
    print("Interest expenses 2015: "+interestExpenses[1])
    interestExpenses.append(dictor(dataset,""+company+".Interest Expense.2016-09"))
    print("Interest expenses 2016: "+interestExpenses[2])
    interestExpenses.append(dictor(dataset,""+company+".Interest Expense.2017-09"))
    print("Interest expenses 2017: "+interestExpenses[3])
    interestExpenses.append(dictor(dataset,""+company+".Interest Expense.2018-09"))
    print("Interest expenses 2018: "+interestExpenses[4])
    interestExpenses.append(dictor(dataset,""+company+".Interest Expense.TTM"))
    print("Interest expenses 2019/TTM: "+interestExpenses[5])
    print("\n")    

def getOtherIncome(company):
    otherIncome.append(dictor(dataset,""+company+".Other income (expense).2014-09"))
    print("Other income 2014: "+otherIncome[0])
    otherIncome.append(dictor(dataset,""+company+".Other income (expense).2015-09"))
    print("Other income 2015: "+otherIncome[1])
    otherIncome.append(dictor(dataset,""+company+".Other income (expense).2016-09"))
    print("Other income 2016: "+otherIncome[2])
    otherIncome.append(dictor(dataset,""+company+".Other income (expense).2017-09"))
    print("Other income 2017: "+otherIncome[3])
    otherIncome.append(dictor(dataset,""+company+".Other income (expense).2018-09"))
    print("Other income 2018: "+otherIncome[4])
    otherIncome.append(dictor(dataset,""+company+".Other income (expense).TTM"))
    print("Other income 2019/TTM: "+otherIncome[5])
    print("\n")    

def getIncomeBeforeTaxes(company):
    incomeBeforeTaxes.append(dictor(dataset,""+company+".Income before taxes.2014-09"))
    print("Income before taxes 2014: "+incomeBeforeTaxes[0])
    incomeBeforeTaxes.append(dictor(dataset,""+company+".Income before taxes.2015-09"))
    print("Income before taxes 2015: "+incomeBeforeTaxes[1])
    incomeBeforeTaxes.append(dictor(dataset,""+company+".Income before taxes.2016-09"))
    print("Income before taxes 2016: "+incomeBeforeTaxes[2])
    incomeBeforeTaxes.append(dictor(dataset,""+company+".Income before taxes.2017-09"))
    print("Income before taxes 2017: "+incomeBeforeTaxes[3])
    incomeBeforeTaxes.append(dictor(dataset,""+company+".Income before taxes.2018-09"))
    print("Income before taxes 2018: "+incomeBeforeTaxes[4])
    incomeBeforeTaxes.append(dictor(dataset,""+company+".Income before taxes.TTM"))
    print("Income before taxes 2019/TTM: "+incomeBeforeTaxes[5])
    print("\n")

def getProvisionForIncomeTaxes(company):
    provisionForIncomeTaxes.append(dictor(dataset,""+company+".Provision for income taxes.2014-09"))
    print("Provision for income taxes 2014: "+provisionForIncomeTaxes[0])
    provisionForIncomeTaxes.append(dictor(dataset,""+company+".Provision for income taxes.2015-09"))
    print("Provision for income taxes 2015: "+provisionForIncomeTaxes[1])
    provisionForIncomeTaxes.append(dictor(dataset,""+company+".Provision for income taxes.2016-09"))
    print("Provision for income taxes 2016: "+provisionForIncomeTaxes[2])
    provisionForIncomeTaxes.append(dictor(dataset,""+company+".Provision for income taxes.2017-09"))
    print("Provision for income taxes 2017: "+provisionForIncomeTaxes[3])
    provisionForIncomeTaxes.append(dictor(dataset,""+company+".Provision for income taxes.2018-09"))
    print("Provision for income taxes 2018: "+provisionForIncomeTaxes[4])
    provisionForIncomeTaxes.append(dictor(dataset,""+company+".Provision for income taxes.TTM"))
    print("Provision for income taxes 2019/TTM: "+provisionForIncomeTaxes[5])
    print("\n")

def getNetIncome(company):
    netIncome.append(dictor(dataset,""+company+".Net income.2014-09"))
    print("Net income 2014: "+netIncome[0])
    netIncome.append(dictor(dataset,""+company+".Net income.2015-09"))
    print("Net income 2015: "+netIncome[1])
    netIncome.append(dictor(dataset,""+company+".Net income.2016-09"))
    print("Net income 2016: "+netIncome[2])
    netIncome.append(dictor(dataset,""+company+".Net income.2017-09"))
    print("Net income 2017: "+netIncome[3])
    netIncome.append(dictor(dataset,""+company+".Net income.2018-09"))
    print("Net income 2018: "+netIncome[4])
    netIncome.append(dictor(dataset,""+company+".Net income.TTM"))
    print("Net income 2019/TTM: "+netIncome[5])
    print("\n")   

# Parameter: company, use ticker names. 'AAPL'.
getRevenue("AAPL")
getCostOfRevenue("AAPL")
getGrossProfit("AAPL")
getResearchAndDevelopment("AAPL")
getSalesAndAdministrative("AAPL")
getOperatingIncome("AAPL")
getInterestExpenses("AAPL")
getOtherIncome("AAPL")
getIncomeBeforeTaxes("AAPL")
getProvisionForIncomeTaxes("AAPL")
getNetIncome("AAPL")
#-----------------------------------------------------------------------------------------------------#
##### Second code segment for the balance sheet #####
url = "https://financialmodelingprep.com/api/financials/balance-sheet-statement/AAPL?datatype=json"
r = request.urlopen(url)
dataset = json.loads(r.read())
print(dataset)
for i in dataset["AAPL"].keys():
    print(i)
print("\n")

# Balance sheet
totalAssets = []
totalLiabilities = []

def getTotalAssets(company):
    totalAssets.append(dictor(dataset,""+company+".Total assets.2014-09"))
    print("Total assets 2014: "+totalAssets[0])
    totalAssets.append(dictor(dataset,""+company+".Total assets.2015-09"))
    print("Total assets 2015: "+totalAssets[1])
    totalAssets.append(dictor(dataset,""+company+".Total assets.2016-09"))
    print("Total assets 2016: "+totalAssets[2])
    totalAssets.append(dictor(dataset,""+company+".Total assets.2017-09"))
    print("Total assets 2017: "+totalAssets[3])
    totalAssets.append(dictor(dataset,""+company+".Total assets.2018-09"))
    print("Total assets 2018: "+totalAssets[4])
    #totalAssets.append(dictor(dataset,""+company+".Total assets.TTM"))
    #print("Total assets 2019/TTM: "+totalAssets[5])
    print("\n")   

def getTotalLiabilities(company):
    totalLiabilities.append(dictor(dataset,""+company+".Total liabilities.2014-09"))
    print("Total liabilities 2014: "+totalLiabilities[0])
    totalLiabilities.append(dictor(dataset,""+company+".Total liabilities.2015-09"))
    print("Total liabilities 2015: "+totalLiabilities[1])
    totalLiabilities.append(dictor(dataset,""+company+".Total liabilities.2016-09"))
    print("Total liabilities 2016: "+totalLiabilities[2])
    totalLiabilities.append(dictor(dataset,""+company+".Total liabilities.2017-09"))
    print("Total liabilities 2017: "+totalLiabilities[3])
    totalLiabilities.append(dictor(dataset,""+company+".Total liabilities.2018-09"))
    print("Total liabilities 2018: "+totalLiabilities[4])
    #totalLiabilities.append(dictor(dataset,""+company+".Total liabilities.TTM"))
    #print("Total liabilities 2019/TTM: "+totalLiabilities[5])
    print("\n")   

getTotalAssets("AAPL")
getTotalLiabilities("AAPL")
#-----------------------------------------------------------------------------------------------------#
# Preparing data for analytical use with company unique up-to-date company data.
revenue = float(revenue[len(revenue)-1])
print(revenue)
cost_of_sale = float(costOfRevenue[len(costOfRevenue)-1])
gross_profit = float(grossProfit[len(grossProfit)-1])
administrative_costs = float(salesAndAdministrative[len(salesAndAdministrative)-1])
other_operation_costs = float(researchAndDevelopment[len(researchAndDevelopment)-1])
operating_profit = float(operatingIncome[len(operatingIncome)-1])
print(operating_profit)
financial_income = float(otherIncome[len(otherIncome)-1])
financial_costs = float(interestExpenses[len(interestExpenses)-1])
result_before_tax = float(incomeBeforeTaxes[len(incomeBeforeTaxes)-1])
taxes = float(provisionForIncomeTaxes[len(provisionForIncomeTaxes)-1])
taxed_result = float(netIncome[len(netIncome)-1])
print(taxed_result)

ga = (float(totalAssets[len(totalAssets)-1])+float(totalAssets[len(totalAssets)-1]))/2
gf = (float(totalLiabilities[len(totalLiabilities)-1])+float(totalLiabilities[len(totalLiabilities)-1]))/2
ge = ga-gf

assets = float(totalAssets[len(totalAssets)-1])
liabilities = float(totalLiabilities[len(totalLiabilities)-1])
equity = assets-liabilities

market_price = 328.3
shares = 1

# Testing with static company data.
# Following is x's financial statement data, TTM.
"""
# Pandora
revenue = 22806
cost_of_sale = 5864
gross_profit = float(revenue - cost_of_sale)
sales_and_distribution_costs = 8222
administrative_costs = 2289
other_operation_costs = 0
operating_profit = float(gross_profit - (sales_and_distribution_costs + administrative_costs + other_operation_costs))
financial_income = 533
financial_costs = 382
result_before_tax = float(operating_profit - financial_costs + financial_income)
taxes = 1537
taxed_result = float(result_before_tax - taxes)

ga = (19244+17428)/2
gf = (12825+10914)/2
ge = (6419+6514)/2

equity = 6419
assets = 19244
liabilities = 12825

market_price = 328.3
shares = 1
"""
"""
# Apple
revenue = 265595
cost_of_sale = 163756
gross_profit = float(revenue - cost_of_sale)
sales_and_distribution_costs = 0
administrative_costs = 0
other_operation_costs = 265595-194697
operating_profit = float(gross_profit - (sales_and_distribution_costs + administrative_costs + other_operation_costs))
financial_income = 2005
financial_costs = 0
result_before_tax = float(operating_profit - financial_costs + financial_income)
taxes = 13372
taxed_result = float(result_before_tax - taxes)

ga = (365725+375319)/2
gf = (258578+241272)/2
ge = (107147+134047)/2

equity = 107147
assets = 365725
liabilities = 258578

market_price = 178.9
shares = 1
"""
