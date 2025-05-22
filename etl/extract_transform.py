# extract_transform.py
import yfinance as yf
import pandas as pd

def get_stock_data(ticker="AOT.BK", period="1mo", interval="1d"):
    data = yf.download(ticker, period=period, interval=interval)
    data['MA7'] = data['Close'].rolling(window=7).mean()
    return data

if __name__ == "__main__":
    df = get_stock_data()
    df.to_csv("stock_data.csv")
