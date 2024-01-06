#STOCK PORTFOLIO TRACKER
#TASK -2


import yfinance as yf
import matplotlib.pyplot as plt
import requests
from datetime import datetime

class StockPortfolioTracker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = {}

    def get_stock_quote(self, symbol):
        base_url = "https://www.alphavantage.co/query"
        function = "GLOBAL_QUOTE"
        params = {"function": function, "symbol": symbol, "apikey": self.api_key }

        response = requests.get(base_url, params=params)
        data = response.json()

        if "Global Quote" in data:
            return data["Global Quote"]
        else:
            print("Error retrieving stock quote.")
            return None

    def add_stock(self, symbol, shares):
        if symbol not in self.portfolio:
            self.portfolio[symbol] = {"Shares": shares, "AveragePrice": 0.0}
            print(f"{symbol} added to the portfolio.")
        else:
            print(f"{symbol} is already in the portfolio. Use update_stock to modify.")

    def update_stock(self, symbol, shares):
        if symbol in self.portfolio:
            total_shares = self.portfolio[symbol]["Shares"] + shares
            self.portfolio[symbol]["Shares"] = total_shares
            print(f"{symbol} updated in the portfolio.")
        else:
            print(f"{symbol} not found in the portfolio. Use add_stock to add.")

    def remove_stock(self, symbol):
        if symbol in self.portfolio:
            del self.portfolio[symbol]
            print(f"{symbol} removed from the portfolio.")
        else:
            print(f"{symbol} not found in the portfolio.")

    def track_portfolio_performance(self):
        total_value = 0.0

        for symbol, details in self.portfolio.items():
            stock_quote = self.get_stock_quote(symbol)

            if stock_quote:
                price_per_share = float(stock_quote["05. price"])
                total_shares = details["Shares"]
                current_value = price_per_share * total_shares
                total_value += current_value

                print(f"{symbol}: {total_shares} shares, Current Price: {price_per_share}, Value: {current_value}")

        print(f"Total Portfolio Value: {total_value:.2f}")

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def plot_stock_data(stock_data, ticker):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label=ticker)
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.legend()
    plt.show()

api_key = '4X4IHDB51X136O03'
portfolio_tracker = StockPortfolioTracker(api_key)

# Example usage:
portfolio_tracker.add_stock("AAPL", 6)
portfolio_tracker.add_stock("GOOGL", 4)
portfolio_tracker.update_stock("AAPL", 7)
portfolio_tracker.add_stock("MSFT", 8)

# Plot individual stocks
start_date = '2023-01-02'
end_date = datetime.today().strftime('%Y-%m-%d')
for stock, quantity in portfolio_tracker.portfolio.items():
    stock_data = get_stock_data(stock, start_date, end_date)
    plot_stock_data(stock_data, stock)

# Plot overall portfolio value
portfolio_tracker.track_portfolio_performance()
