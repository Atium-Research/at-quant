import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_stock_prices(start: dt.date, end: dt.date) -> pl.DataFrame:
    """Load stock price data within a date range.

    Stock prices contain historical price data (typically close prices, but may include
    open, high, low, volume). This is fundamental market data used for return calculations,
    backtesting, and signal generation.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.

    Returns:
        DataFrame containing stock prices sorted by date and ticker.
        The 'year' column is dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('stock_prices')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )

def get_stock_prices_schema() -> pl.Schema:
    """Get the schema of the stock_prices table.

    Returns:
        Polars Schema object describing the structure of the stock_prices table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('stock_prices')
    )
