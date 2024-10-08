# use https://pypi.org/project/yfinance/
# install : pip install yfinance --upgrade --no-cache-dir
from datetime import datetime

import yfinance as yf

class Quote:
    def __init__(self, ticker):
        self.ticker = ticker
        self.quote = yf.Ticker(ticker)

    # get all stock info
    def info(self):
        return self.quote.info

    def get_name(self):
        return self.quote.info['shortName']

    # get the symbol
    def get_symbol(self):
        return self.quote.info['symbol']

    def get_exchange(self):
        return self.quote.info['exchange']

    def get_currency(self):
        return self.quote.info['currency']


    def get_previous_close(self):
        """
        Previous close price from info
        """
        return self.quote.info['previousClose']

    # get historical market data
    def historical_market_data(self, period="1mo"):
        # Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        hist = self.quote.history(period=period)
        return hist


    def get_last_close(self):
        """
        Last close from historical data
        return last_close_value, last_close_date
        """
        df_data1 = self.historical_market_data("1d")
        last_close_value = float(df_data1['Close'].iloc[-1])
        last_close_date = df_data1['Close'].index[-1]
        return last_close_value, last_close_date


if __name__ == '__main__':
    quote_MSFT = Quote("MSFT")
    info = quote_MSFT.info()
    # print(type(info))
    # print(info)
    # {'address1': 'One Microsoft Way', 'city': 'Redmond', 'state': 'WA', 'zip': '98052-6399', 'country': 'United States',
    # 'phone': '425 882 8080', 'website': 'https://www.microsoft.com', 'industry': 'Software - Infrastructure', 'industryKey': 'software-infrastructure',
    # 'industryDisp': 'Software - Infrastructure', 'sector': 'Technology', 'sectorKey': 'technology', 'sectorDisp': 'Technology',
    # 'longBusinessSummary': 'Microsoft Corporation develops and supports software, services, devices and solutions worldwide.
    # The Productivity and Business Processes segment offers office, exchange, SharePoint, Microsoft Teams, office 365 Security and Compliance, Microsoft viva, and Microsoft 365 copilot;
    # and office consumer services, such as Microsoft 365 consumer subscriptions, Office licensed on-premises, and other office services. This segment also provides LinkedIn;
    # and dynamics business solutions, including Dynamics 365, a set of intelligent, cloud-based applications across ERP, CRM, power apps, and power automate;
    # and on-premises ERP and CRM applications. The Intelligent Cloud segment offers server products and cloud services, such as azure and other cloud services;
    # SQL and windows server, visual studio, system center, and related client access licenses, as well as nuance and GitHub; and enterprise services including enterprise support services,
    # industry solutions, and nuance professional services. The More Personal Computing segment offers Windows, including windows OEM licensing and other non-volume
    # licensing of the Windows operating system; Windows commercial comprising volume licensing of the Windows operating system, windows cloud services,
    # and other Windows commercial offerings; patent licensing; and windows Internet of Things; and devices, such as surface, HoloLens, and PC accessories.
    # Additionally, this segment provides gaming, which includes Xbox hardware and content, and first- and third-party content; Xbox game pass and other subscriptions,
    # cloud gaming, advertising, third-party disc royalties, and other cloud services; and search and news advertising, which includes Bing, Microsoft News and Edge,
    # and third-party affiliates. The company sells its products through OEMs, distributors, and resellers; and directly through digital marketplaces, online, and retail stores.
    # The company was founded in 1975 and is headquartered in Redmond, Washington.',
    # 'fullTimeEmployees': 228000,
    # 'companyOfficers': [{'maxAge': 1, 'name': 'Mr. Satya  Nadella', 'age': 56, 'title': 'Chairman & CEO', 'yearBorn': 1967, 'fiscalYear': 2023, 'totalPay': 9276400, 'exercisedValue': 0,
    # 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Bradford L. Smith LCA', 'age': 64, 'title': 'President & Vice Chairman', 'yearBorn': 1959, 'fiscalYear': 2023, 'totalPay': 3591277, 'exercisedValue': 0,
    # 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Ms. Amy E. Hood', 'age': 51, 'title': 'Executive VP & CFO', 'yearBorn': 1972, 'fiscalYear': 2023, 'totalPay': 3452196, 'exercisedValue': 0, 'unexercisedValue': 0},
    # {'maxAge': 1, 'name': 'Mr. Judson B. Althoff', 'age': 50, 'title': 'Executive VP & Chief Commercial Officer', 'yearBorn': 1973, 'fiscalYear': 2023, 'totalPay': 3355797, 'exercisedValue': 0, 'unexercisedValue': 0},
    # {'maxAge': 1, 'name': 'Mr. Christopher David Young', 'age': 51, 'title': 'Executive Vice President of Business Development, Strategy & Ventures', 'yearBorn': 1972, 'fiscalYear': 2023, 'totalPay': 2460507, 'exercisedValue': 0, 'unexercisedValue': 0},
    # {'maxAge': 1, 'name': 'Ms. Alice L. Jolla', 'age': 57, 'title': 'Corporate VP & Chief Accounting Officer', 'yearBorn': 1966, 'fiscalYear': 2023, 'exercisedValue': 0, 'unexercisedValue': 0},
    # {'maxAge': 1, 'name': 'Mr. James Kevin Scott', 'age': 51, 'title': 'Executive VP of AI & CTO', 'yearBorn': 1972, 'fiscalYear': 2023, 'exercisedValue': 0, 'unexercisedValue': 0},
    # {'maxAge': 1, 'name': 'Brett  Iversen', 'title': 'Vice President of Investor Relations', 'fiscalYear': 2023, 'exercisedValue': 0, 'unexercisedValue': 0},
    # {'maxAge': 1, 'name': 'Mr. Hossein  Nowbar', 'title': 'Chief Legal Officer', 'fiscalYear': 2023, 'exercisedValue': 0, 'unexercisedValue': 0},
    # {'maxAge': 1, 'name': 'Mr. Frank X. Shaw', 'title': 'Chief Communications Officer', 'fiscalYear': 2023, 'exercisedValue': 0, 'unexercisedValue': 0}],
    # 'auditRisk': 3, 'boardRisk': 4, 'compensationRisk': 2, 'shareHolderRightsRisk': 2, 'overallRisk': 1, 'governanceEpochDate': 1725148800,
    # 'compensationAsOfEpochDate': 1703980800, 'irWebsite': 'http://www.microsoft.com/investor/default.aspx',
    # 'maxAge': 86400, 'priceHint': 2, 'previousClose': 423.04, 'open': 423.34, 'dayLow': 420.66, 'dayHigh': 424.01,
    # 'regularMarketPreviousClose': 423.04, 'regularMarketOpen': 423.34, 'regularMarketDayLow': 420.66, 'regularMarketDayHigh': 424.01,
    # 'dividendRate': 3.0, 'dividendYield': 0.0070999996, 'exDividendDate': 1723680000, 'payoutRatio': 0.2483,
    # 'fiveYearAvgDividendYield': 0.9, 'beta': 0.896, 'trailingPE': 35.714405, 'forwardPE': 27.689224, 'volume': 1174603,
    # 'regularMarketVolume': 1174603, 'averageVolume': 19836953, 'averageVolume10days': 17961360, 'averageDailyVolume10Day': 17961360,
    # 'bid': 420.84, 'ask': 421.9, 'bidSize': 400, 'askSize': 400, 'marketCap': 3132505980928, 'fiftyTwoWeekLow': 309.45, 'fiftyTwoWeekHigh': 468.35,
    # 'priceToSalesTrailing12Months': 12.779375, 'fiftyDayAverage': 425.756, 'twoHundredDayAverage': 411.9642, 'trailingAnnualDividendRate': 3.0,
    # 'trailingAnnualDividendYield': 0.007091528, 'currency': 'USD', 'enterpriseValue': 3166793629696, 'profitMargins': 0.35956, 'floatShares': 7422706458,
    # 'sharesOutstanding': 7433039872, 'sharesShort': 54789102, 'sharesShortPriorMonth': 61931266, 'sharesShortPreviousMonthDate': 1721001600,
    # 'dateShortInterest': 1723680000, 'sharesPercentSharesOut': 0.0074, 'heldPercentInsiders': 0.00054000004, 'heldPercentInstitutions': 0.7374, 'shortRatio': 2.37,
    # 'shortPercentOfFloat': 0.0074, 'impliedSharesOutstanding': 7433039872, 'bookValue': 36.115, 'priceToBook': 11.669112, 'lastFiscalYearEnd': 1719705600,
    # 'nextFiscalYearEnd': 1751241600, 'mostRecentQuarter': 1719705600, 'earningsQuarterlyGrowth': 0.097, 'netIncomeToCommon': 88135999488, 'trailingEps': 11.8,
    # 'forwardEps': 15.22, 'pegRatio': 2.22, 'lastSplitFactor': '2:1', 'lastSplitDate': 1045526400, 'enterpriseToRevenue': 12.919, 'enterpriseToEbitda': 24.467,
    # '52WeekChange': 0.24901092, 'SandP52WeekChange': 0.23285389, 'lastDividendValue': 0.75, 'lastDividendDate': 1723680000,
    # 'exchange': 'NMS', 'quoteType': 'EQUITY', 'symbol': 'MSFT', 'underlyingSymbol': 'MSFT',
    # 'shortName': 'Microsoft Corporation', 'longName': 'Microsoft Corporation', 'firstTradeDateEpochUtc': 511108200,
    # 'timeZoneFullName': 'America/New_York', 'timeZoneShortName': 'EDT', 'uuid': 'b004b3ec-de24-385e-b2c1-923f10d3fb62',
    # 'messageBoardId': 'finmb_21835', 'gmtOffSetMilliseconds': -14400000, 'currentPrice': 421.43, 'targetHighPrice': 600.0,
    # 'targetLowPrice': 440.0, 'targetMeanPrice': 496.67, 'targetMedianPrice': 500.0, 'recommendationMean': 1.7, 'recommendationKey': 'buy',
    # 'numberOfAnalystOpinions': 47, 'totalCash': 75531001856, 'totalCashPerShare': 10.162, 'ebitda': 129433001984, 'totalDebt': 97851998208,
    # 'quickRatio': 1.141, 'currentRatio': 1.275, 'totalRevenue': 245122007040, 'debtToEquity': 36.447, 'revenuePerShare': 32.986, 'returnOnAssets': 0.14802,
    # 'returnOnEquity': 0.37133, 'freeCashflow': 56705249280, 'operatingCashflow': 118547996672, 'earningsGrowth': 0.097, 'revenueGrowth': 0.152, 'grossMargins': 0.69764,
    # 'ebitdaMargins': 0.52804, 'operatingMargins': 0.43143, 'financialCurrency': 'USD', 'trailingPegRatio': 2.2815}

    # get data from info (raw)
    # print the adress
    print(info['address1'])
    # print the symbol
    print(info['symbol'])


    # get data from info and get_XXX
    # get the symbol
    print(quote_MSFT.get_symbol())
    # get the previous close
    print(quote_MSFT.get_previous_close())


    # historical market data
    hist_MSFT = quote_MSFT.historical_market_data()
    # print(type(hist_MSFT)) #<class 'pandas.core.frame.DataFrame'>
    # print(hist_MSFT.shape) # 22,7
    # print(list(hist_MSFT.columns)) #['Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']

    # get the last close
    print(quote_MSFT.get_last_close())