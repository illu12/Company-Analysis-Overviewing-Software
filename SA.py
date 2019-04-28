#############################
#// Stock Analysis Module //#
#############################

def EPS(a,b):
    """Netincome-dividends/outstanding shares"""
    """ profit / shares """
    return a/b
def absolutePE(a,b):
    """ P/E of current stock price """
    """ Price/earnings """
    return a/b
def relativePE():
    """ P/E of a stock price over a longer period """
    return 1
def ROE():
    """ Return on Equity """
    """ Netincome/shareholders equity """
    return a/b
def ROA():
    """ Return on Assets """
    """ Netincome/total assets """
    return a/b
def ROI():
    """ Return on Investment """
    """ Gains-costs/costs """
    return (a-b)/b
def beta():
    """ The volatile level of the stock, relatively to the average market stock """
    """ b < 1, less volatile than market average stocks """
    """ b = 1, equally volatile than market average stocks """
    """ b > 1, more volatile than market average stocks """
    return 1
def marketCap(a,b):
    """ Market valuation of a company """
    """ Stock price*outstanding stocks """
    return a*b
def intrinsicValue(a,b):
    """ Theoretical value of a stock """
    """ Equity/total stocks """
    return a/b
def Delta(a,b):
    """ Difference in market price vs. intrinsic value """
    return b-a

"""
ROA - https://www.investopedia.com/terms/r/returnonassets.asp
ROE - https://www.investopedia.com/terms/r/returnonequity.asp
ROI - https://www.investopedia.com/terms/r/returnoninvestment.asp
"""
