from binance.um_futures import UMFutures

API_KEY = "API_KEY"
SECRET = "API_SECRET"

client = UMFutures(key=API_KEY, secret=SECRET, base_url="https://testnet.binancefuture.com")

try:
    print("Ping:", client.ping())
    balance = client.account()
    print("\nCONNECTED SUCCESSFULLY ✅")
    print(balance)

except Exception as e:
    print("❌ ERROR:", e)
