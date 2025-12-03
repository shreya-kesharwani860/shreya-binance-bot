from binance.um_futures import UMFutures

API_KEY = "zgEdijg4vDQ7r564Itf2KjZK6OGuXDuy4E1B8Ya2j12J4rj52171xH6NqNI7LcZQ"
SECRET = "VwQ1mGiKJKr7Nx1zTNa5QWMbSN9YunI8FbiY2o9H7kt5dztPBmXpEdtHzFSZM03L"

client = UMFutures(key=API_KEY, secret=SECRET, base_url="https://testnet.binancefuture.com")

try:
    print("Ping:", client.ping())
    balance = client.account()
    print("\nCONNECTED SUCCESSFULLY ✅")
    print(balance)

except Exception as e:
    print("❌ ERROR:", e)
