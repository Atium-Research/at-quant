import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_etf_prices(start: dt.date, end: dt.date) -> pl.DataFrame:
    """Load ETF (Exchange-Traded Fund) price data within a date range.

    ETF prices represent the market value of exchange-traded funds, which are
    investment vehicles that track indices, sectors, commodities, or other assets.
    This data is used for performance analysis and portfolio construction.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.

    Returns:
        DataFrame containing ETF prices sorted by date and ticker.
        The 'year' column is dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('etf_prices')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )

def get_etf_prices_schema() -> pl.Schema:
    """Get the schema of the etf_prices table.

    Returns:
        Polars Schema object describing the structure of the etf_prices table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('etf_prices')
    )
