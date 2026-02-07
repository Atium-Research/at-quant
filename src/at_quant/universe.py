import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_universe(start: dt.date, end: dt.date) -> pl.DataFrame:
    """Load the trading universe definition within a date range.

    The universe defines which stocks are eligible for trading on each date,
    based on liquidity, market cap, listing status, and other criteria. This is
    used to filter stocks for strategy backtesting and portfolio construction.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.

    Returns:
        DataFrame containing universe membership sorted by date and ticker.
        The 'year' column is dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('universe')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )

def get_universe_schema() -> pl.Schema:
    """Get the schema of the universe table.

    Returns:
        Polars Schema object describing the structure of the universe table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('universe')
    )
