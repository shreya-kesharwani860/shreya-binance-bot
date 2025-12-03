# Binance Futures Trading Bot

## Overview
This is a CLI-based trading bot for Binance USDT-M Futures. The bot supports **market orders**, **limit orders**, and **TWAP orders**. It includes logging, validation, and error handling to ensure safe and structured trading.

---

## Features

- **Market Orders:** Buy or sell immediately at the current market price.
- **Limit Orders:** Place an order at a specific price.
- **TWAP Orders:** Split a large order into smaller chunks executed over time intervals.
- **Logging:** All actions, API requests, and errors are logged in `bot.log`.
- **Validation:** Validates symbol, order side, quantity, and price input.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your_username>/<repo_name>.git
cd <repo_name>
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file in the project root with your Binance API credentials:

env
Copy code
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
TESTNET_BASE_URL=https://testnet.binancefuture.com
Usage
Run the CLI interface:

bash
Copy code
python -m src.cli
Follow the interactive menu:

Market Order

Limit Order

TWAP Order

Example inputs:

Symbol: BTCUSDT

Side: BUY or SELL

Quantity: 0.002

Limit price: 92300 (for limit orders)

TWAP intervals: 5 (for TWAP)

Interval seconds: 60 (for TWAP)

Project Structure
css
Copy code
[project_root]/
│
├── src/
│   ├── market_orders.py
│   ├── limit_orders.py
│   ├── cli.py
│   └── advanced/
│       ├── twap.py
│
├── bot.log
├── README.md
├── report.pdf (optional)
└── requirements.txt
Logging
All API requests, executions, and errors are logged in bot.log with timestamps for easy tracking.

Notes
Do NOT commit your .env file containing API keys to GitHub.

This bot uses the Binance Testnet by default.

Ensure Python 3.11+ is installed.