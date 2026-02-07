import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_etf_returns(start: dt.date, end: dt.date) -> pl.DataFrame:
    """Load ETF return data within a date range.

    ETF returns represent the percentage change in ETF prices over time,
    used for performance analysis, factor modeling, and portfolio optimization.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.

    Returns:
        DataFrame containing ETF returns sorted by date and ticker.
        The 'year' column is dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('etf_returns')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )

def get_etf_returns_schema() -> pl.Schema:
    """Get the schema of the etf_returns table.

    Returns:
        Polars Schema object describing the structure of the etf_returns table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('etf_returns')
    )
