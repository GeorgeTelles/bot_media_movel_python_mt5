<div>
  <img src="https://raw.githubusercontent.com/GeorgeTelles/georgetelles/f69531ec6b293b5148563588a764c010015d315e/logo_clara.png" alt="logo clara" width="300" style="display: inline-block; vertical-align: top; margin-right: 10px;">
  <img src="https://raw.githubusercontent.com/GeorgeTelles/georgetelles/f69531ec6b293b5148563588a764c010015d315e/logo_dark.png" alt="logo dark" width="300" style="display: inline-block; vertical-align: top;">
</div>

# Moving Average Crossover Trading Bot

This trading bot analyzes the moving average of a financial instrument and executes trades based on price movements relative to the moving average. Specifically, the bot places a buy order when the price crosses above the moving average and closes the position when the price crosses below it.

## Features

- **Real-Time Analysis**: Continuously fetches and analyzes the latest market data using MetaTrader 5.
- **Moving Average Calculation**: Computes a 9-period simple moving average (SMA) for the specified symbol.
- **Trade Execution**: 
  - Places a buy order when the current price is above the moving average and no positions are currently open.
  - Closes the position when the current price is below the moving average and an open position exists.
- **Logging**: Prints status updates including the number of open positions, current moving average, and current price.
- **Interval-Based Execution**: Checks the conditions and performs actions every 10 seconds.

## Requirements

- **Python**: Version 3.x
- **MetaTrader5 Library**: Install via pip with `pip install MetaTrader5`.
- **Pandas Library**: Install via pip with `pip install pandas`.
- **Pandas TA Library**: Install via pip with `pip install pandas_ta`.

## Usage

1. **Initialization**: Connects to the MetaTrader 5 terminal.
2. **Data Retrieval**: Fetches the latest minute-level (M1) data for the specified symbol.
3. **Moving Average Calculation**: Calculates the 9-period simple moving average using the retrieved data.
4. **Order Execution**:
   - **Buy Order**: Sends a buy order if the price is above the moving average and no positions are open.
   - **Sell Order**: Sends a sell order to close the position if the price is below the moving average.
5. **Operation Loop**: Runs an infinite loop, checking the conditions and executing trades every 10 seconds.

## Author

- **George Telles**
- Contact: +55 11 93290-7425

