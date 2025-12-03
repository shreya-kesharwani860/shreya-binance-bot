
import os
import logging
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv('API_KEY')
API_SECRET=os.getenv('API_SECRET')
TESTNET_BASE_URL=os.getenv('TESTNET_BASE_URL','https://testnet.binancefuture.com')

def setup_logging():
    logger=logging.getLogger('bot')
    logger.setLevel(logging.INFO)
    fh=logging.FileHandler('bot.log')
    formatter=logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

def validate_symbol(symbol):
    return isinstance(symbol,str) and symbol.isalnum()

def validate_side(side):
    return side.upper() in ('BUY','SELL')

def validate_qty(qty):
    try:
        q=float(qty)
        return q>0
    except:
        return False

