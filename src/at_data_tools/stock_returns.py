import datetime as dt

import bear_lake as bl
import polars as pl

from at_data_tools.clients import get_bear_lake_client


def load_stock_returns(start: dt.date, end: dt.date) -> pl.DataFrame:
    """Load stock return data within a date range.

    Stock returns represent the percentage change in stock prices over time.
    This is the primary data for backtesting trading strategies, performance
    attribution, and risk analysis.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.

    Returns:
        DataFrame containing stock returns sorted by date and ticker.
        The 'year' column is dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('stock_returns')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )

def get_stock_returns_schema() -> pl.Schema:
    """Get the schema of the stock_returns table.

    Returns:
        Polars Schema object describing the structure of the stock_returns table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('stock_returns')
    )
