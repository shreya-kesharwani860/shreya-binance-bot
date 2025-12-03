from binance.um_futures import UMFutures
from .utils import setup_logging, validate_symbol, validate_side, validate_qty, API_KEY, API_SECRET, TESTNET_BASE_URL


logger = setup_logging()

class MarketOrderExecutor:
    def __init__(self, key=None, secret=None, base_url=None):
        self.key = key or API_KEY
        self.secret = secret or API_SECRET
        self.base_url = base_url or TESTNET_BASE_URL
        self.client = UMFutures(key=self.key, secret=self.secret, base_url=self.base_url)

    def place_market_order(self, symbol, side, quantity):
        if not validate_symbol(symbol):
            return {'error': 'invalid symbol'}
        if not validate_side(side):
            return {'error': 'invalid side'}
        if not validate_qty(quantity):
            return {'error': 'invalid quantity'}
        try:
            resp = self.client.new_order(symbol=symbol, side=side.upper(), type='MARKET', quantity=quantity)
            logger.info(f'MARKET order placed {symbol} {side} {quantity} resp={resp}')
            return resp
        except Exception as e:
            logger.exception('MARKET order failed')
            return {'error': str(e)}