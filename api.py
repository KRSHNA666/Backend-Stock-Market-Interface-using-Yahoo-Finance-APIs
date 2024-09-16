import yfinance as yf

def fetch_real_time_price(symbol):
    try:
        stock = yf.Ticker(symbol + ".NS")  # Append ".NS" for stocks listed on the National Stock Exchange (NSE)
        current_price = stock.history(period='1d')['Close'].iloc[-1]
        return current_price
    except Exception as e:
        print(f"Error fetching real-time price for {symbol}: {e}")
        return None

def calculate_profit(buy_price, current_price, shares):
    if buy_price is None or current_price is None:
        return None
    return (current_price - buy_price) * shares

def main():
    symbol = input("Enter the stock symbol (e.g., TCS, INFY): ")
    buy_price = float(input("Enter the buy price per share: "))
    shares = int(input("Enter the number of shares: "))

    current_price = fetch_real_time_price(symbol)
    profit = calculate_profit(buy_price, current_price, shares) 

    print(f"Real-time price for {symbol}: {current_price}")
    if profit is not None:
        print(f"Profit generated after listing: {profit}")

if __name__ == "__main__":
    main()
