import numpy as np
import pandas as pd
import yfinance as yf
import plotly.express as px

def main():
    sym = input("Enter symbol of stock: ")
    period = input("Enter period of report (1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo): ")
    interval = input("Enter interval of report (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo): ")
    createReport(sym, period, interval)

def createReport(sym, period, interval):
    data = yf.download(tickers=sym, period=period, interval=interval)

    high = []
    low = []
    date = []

    for i in data["High"]:
        high.append(i)
    df_1 = pd.DataFrame(high)

    for i in data["Low"]:
        low.append(i)
    df_2 = pd.DataFrame(low)

    highGraph = px.scatter(df_1, trendline="ols", title="Highest prices per interval")
    lowGraph = px.scatter(df_2, trendline="ols", title="Lowest prices per interval")

    highOls = px.get_trendline_results(highGraph).px_fit_results.iloc[0]
    lowOls = px.get_trendline_results(lowGraph).px_fit_results.iloc[0]

    highB = highOls.params[0]
    highM = highOls.params[1]

    lowB = lowOls.params[0]
    lowM = lowOls.params[1]

    print("Predicted High: ")
    print(highM * (len(high)+1) + highB )
    print("Predicted Low: ")
    print(lowM * (len(low)+1) + lowB )

    highGraph.show()
    lowGraph.show()


main()