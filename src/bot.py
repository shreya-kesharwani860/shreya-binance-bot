
import argparse
import os
from market_orders import place_market_order
from limit_orders import place_limit_order
from advanced.oco import place_oco
from advanced.twap import run_twap
from utils import load_client, setup_logging

logger = setup_logging()

parser = argparse.ArgumentParser()
parser.add_argument('type', choices=['MARKET','LIMIT','OCO','TWAP'])
parser.add_argument('symbol')
parser.add_argument('side', choices=['BUY','SELL'], nargs='?')
parser.add_argument('quantity', nargs='?')
parser.add_argument('--price')
parser.add_argument('--stop_price')
parser.add_argument('--interval', type=int, default=60)
parser.add_argument('--chunks', type=int, default=5)
args = parser.parse_args()

API_KEY = os.getenv('zgEdijg4vDQ7r564Itf2KjZK6OGuXDuy4E1B8Ya2j12J4rj52171xH6NqNI7LcZQ')
API_SECRET = os.getenv('VwQ1mGiKJKr7Nx1zTNa5QWMbSN9YunI8FbiY2o9H7kt5dztPBmXpEdtHzFSZM03L')
if not API_KEY or not API_SECRET:
    logger.error('API key/secret not found in environment variables')
    raise SystemExit(1)

client = load_client(API_KEY, API_SECRET)

if args.type == 'MARKET':
    if not args.side or not args.quantity:
        logger.error('MARKET requires side and quantity')
        raise SystemExit(1)
    resp = place_market_order(client, args.symbol, args.side, args.quantity)
    print(resp)

elif args.type == 'LIMIT':
    if not args.side or not args.quantity or not args.price:
        logger.error('LIMIT requires side, quantity and price')
        raise SystemExit(1)
    resp = place_limit_order(client, args.symbol, args.side, args.quantity, args.price)
    print(resp)

elif args.type == 'OCO':
    if not args.side or not args.quantity or not args.price or not args.stop_price:
        logger.error('OCO requires side, quantity, price (take-profit) and stop_price (stop-loss)')
        raise SystemExit(1)
    resp = place_oco(client, args.symbol, args.side, args.quantity, args.price, args.stop_price)
    print(resp)

elif args.type == 'TWAP':
    if not args.side or not args.quantity:
        logger.error('TWAP requires side and quantity')
        raise SystemExit(1)
    resp = run_twap(client, args.symbol, args.side, float(args.quantity), args.chunks, args.interval)
    print(resp)
