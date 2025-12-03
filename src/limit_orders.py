from binance.um_futures import UMFutures
from .utils import setup_logging, validate_symbol, validate_side, validate_qty, API_KEY, API_SECRET, TESTNET_BASE_URL


logger = setup_logging()

class LimitOrderExecutor:
    def __init__(self, key=None, secret=None, base_url=None):
        self.key = key or API_KEY
        self.secret = secret or API_SECRET
        self.base_url = base_url or TESTNET_BASE_URL
        self.client = UMFutures(key=self.key, secret=self.secret, base_url=self.base_url)

    def place_limit_order(self, symbol, side, quantity, price, time_in_force='GTC'):
        if not validate_symbol(symbol):
            return {'error': 'invalid symbol'}
        if not validate_side(side):
            return {'error': 'invalid side'}
        if not validate_qty(quantity):
            return {'error': 'invalid quantity'}
        try:
            resp = self.client.new_order(symbol=symbol, side=side.upper(), type='LIMIT', quantity=quantity, price=price, timeInForce=time_in_force)
            logger.info(f'LIMIT order placed {symbol} {side} {quantity}@{price} resp={resp}')
            return resp
        except Exception as e:
            logger.exception('LIMIT order failed')
            return {'error': str(e)}