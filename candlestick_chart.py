# candlestick_chart.py

import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import yfinance as yf
from stock_prediction import COMPANY, TRAIN_START, TRAIN_END

TEST_START, TEST_END = "2024-04-01", "2024-08-01"

def get_stock_data(company, start_date, end_date):
    """
    Fetch stock data for the given company and date range.
    """
    data = yf.download(company, start=start_date, end=end_date)
    return data

def plot_candlestick_chart(data, title):
    """
    Create and display a candlestick chart using the given data.
    """
    mpf.plot(data, type='candle', style='charles',
             title=title,
             ylabel='Price',
             volume=True,
             figsize=(12, 8))
    plt.show()

if __name__ == "__main__":
    # Fetch data for both training and testing periods
    # train_data = get_stock_data(COMPANY, TRAIN_START, TRAIN_END)
    test_data = get_stock_data(COMPANY, TEST_START, TEST_END)

    # Combine the data
    # full_data = pd.concat([train_data, test_data])

    # Plot candlestick chart for the entire period
    # plot_candlestick_chart(full_data, f"{COMPANY} Stock Price")

    # Plot candlestick chart for just the test period
    plot_candlestick_chart(test_data, f"{COMPANY} Stock Price (2024)")