from binance.um_futures import UMFutures
from src.utils import setup_logging, validate_symbol, validate_qty, API_KEY, API_SECRET, TESTNET_BASE_URL
import math

logger = setup_logging()

# Helper to round price/quantity to symbol precision
def round_step(value, step):
    return round(math.floor(value / step) * step, 8)

class OCOExecutor:
    def __init__(self, key=None, secret=None, base_url=None):
        self.key = key or API_KEY
        self.secret = secret or API_SECRET
        self.base_url = base_url or TESTNET_BASE_URL
        self.client = UMFutures(key=self.key, secret=self.secret, base_url=self.base_url)

    def place_oco(self, symbol, side, quantity, price=None, stopPrice=None, stopLimitPrice=None):
        if not validate_symbol(symbol):
            return {'error': 'invalid symbol'}
        if not validate_qty(quantity):
            return {'error': 'invalid quantity'}

        info = self.client.exchange_info()
        symbol_info = next(s for s in info['symbols'] if s['symbol'] == symbol)
        tick_size = float(next(f['tickSize'] for f in symbol_info['filters'] if f['filterType'] == 'PRICE_FILTER'))
        step_size = float(next(f['stepSize'] for f in symbol_info['filters'] if f['filterType'] == 'LOT_SIZE'))

        # Get current price
        price_data = self.client.ticker_price(symbol=symbol)
        current_price = float(price_data['price'])
        logger.info(f'Current {symbol} price: {current_price}')

        # Auto-calculate TP and SL if not provided
        if side.upper() == 'SELL':
            price = price or round_step(current_price * 0.995, tick_size)          # TP slightly below market
            stopPrice = stopPrice or round_step(current_price * 1.005, tick_size) # SL slightly above market
        else:
            price = price or round_step(current_price * 1.005, tick_size)
            stopPrice = stopPrice or round_step(current_price * 0.995, tick_size)

        quantity = round_step(quantity, step_size)

        stop_side = 'BUY' if side.upper() == 'SELL' else 'SELL'

        try:
            # Take Profit LIMIT
            tp = self.client.new_order(
                symbol=symbol,
                side=side.upper(),
                type='LIMIT',
                quantity=quantity,
                price=price,
                timeInForce='GTC'
            )
            # Stop Loss STOP_MARKET
            sl = self.client.new_order(
                symbol=symbol,
                side=stop_side,
                type='STOP_MARKET',
                stopPrice=stopPrice,
                quantity=quantity
            )
            logger.info(f'OCO placed {symbol} {side} {quantity} TP={price} SL={stopPrice} resp={{tp: {tp}, sl: {sl}}}')
            return {'take_profit': tp, 'stop_loss': sl}
        except Exception as e:
            logger.exception('OCO order failed')
            return {'error': str(e)}
