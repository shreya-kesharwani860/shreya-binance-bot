## Setup

1. Create a Binance Futures Testnet account and get API key & secret.
2. Set environment variables:

```bash
export BINANCE_API_KEY="your_key"
export BINANCE_API_SECRET="your_secret"
````

3. Install requirements:

```bash
python -m pip install -r requirements.txt
```

4. Usage examples:

```bash
python src/bot.py MARKET BTCUSDT BUY 0.001
python src/bot.py LIMIT BTCUSDT SELL 0.001 --price 60000
python src/bot.py OCO BTCUSDT SELL 0.001 --price 65000 --stop_price 59000
python src/bot.py TWAP BTCUSDT BUY 0.01 --chunks 5 --interval 60
```

## Notes

* The bot uses Binance Futures Testnet base URL and `futures_create_order` endpoints.
* Logs are written to `bot.log`.

zgEdijg4vDQ7r564Itf2KjZK6OGuXDuy4E1B8Ya2j12J4rj52171xH6NqNI7LcZQ

VwQ1mGiKJKr7Nx1zTNa5QWMbSN9YunI8FbiY2o9H7kt5dztPBmXpEdtHzFSZM03L