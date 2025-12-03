import argparse
from src.market_orders import MarketOrderExecutor
from src.limit_orders import LimitOrderExecutor
from src.advanced.oco import OCOExecutor

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='order_type')

# Market
p_market = subparsers.add_parser('market')
p_market.add_argument('symbol')
p_market.add_argument('side')
p_market.add_argument('quantity', type=float)

# Limit
p_limit = subparsers.add_parser('limit')
p_limit.add_argument('symbol')
p_limit.add_argument('side')
p_limit.add_argument('quantity', type=float)
p_limit.add_argument('price', type=float)

# OCO
p_oco = subparsers.add_parser('oco')
p_oco.add_argument('symbol')
p_oco.add_argument('side')
p_oco.add_argument('quantity', type=float)
p_oco.add_argument('--price', type=float, default=None)
p_oco.add_argument('--stopPrice', type=float, default=None)
p_oco.add_argument('--stopLimitPrice', type=float, default=None)

args = parser.parse_args()

if args.order_type == 'market':
    exe = MarketOrderExecutor()
    resp = exe.place_market_order(args.symbol, args.side, args.quantity)
    print('📌 RESULT:', resp)

elif args.order_type == 'limit':
    exe = LimitOrderExecutor()
    resp = exe.place_limit_order(args.symbol, args.side, args.quantity, args.price)
    print('📌 RESULT:', resp)

elif args.order_type == 'oco':
    exe = OCOExecutor()
    resp = exe.place_oco(args.symbol, args.side, args.quantity, args.price, args.stopPrice, args.stopLimitPrice)
    print('📌 RESULT:', resp)

else:
    parser.print_help()
