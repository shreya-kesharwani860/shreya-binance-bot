# src/cli.py
from .advanced.twap import TWAPBot
from .market_orders import MarketOrderExecutor
from .limit_orders import LimitOrderExecutor


import logging

logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s'
)

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

def main():
    print("=== Binance Futures Trading Bot CLI ===\n")
    print("1. Market Order")
    print("2. Limit Order")
    print("3. TWAP Order")
    choice = input("Select order type (1-3): ")

    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    qty = float(input("Enter quantity: "))

    if choice == '1':
        bot = MarketOrderExecutor(API_KEY, API_SECRET)
        bot.place_market_order(symbol, side, qty)

    elif choice == '2':
        price = float(input("Enter limit price: "))
        bot = LimitOrderExecutor(API_KEY, API_SECRET)
        bot.place_limit_order(symbol, side, qty, price)

    elif choice == '3':
        intervals = int(input("Enter number of TWAP intervals: "))
        interval_seconds = int(input("Enter interval in seconds: "))
        bot = TWAPBot(API_KEY, API_SECRET)
        bot.place_twap_order(symbol, side, qty, intervals, interval_seconds)

    else:
        print("Invalid selection")

if __name__ == "__main__":
    main()
