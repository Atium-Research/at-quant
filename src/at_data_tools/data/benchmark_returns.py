import datetime as dt

import bear_lake as bl
import polars as pl

from at_data_tools.clients import get_bear_lake_client


def load_benchmark_returns(start: dt.date, end: dt.date) -> pl.DataFrame:
    """Load benchmark returns data within a date range.

    Benchmark returns represent the performance of market indices or other reference
    portfolios used to evaluate trading strategies and portfolio performance.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.

    Returns:
        DataFrame containing benchmark returns sorted by date.
    """
    return (
        get_bear_lake_client().query(
            bl.table('benchmark_returns')
            .filter(pl.col('date').is_between(start, end))
            .sort('date')
        )
    )

def get_benchmark_returns_schema() -> pl.Schema:
    """Get the schema of the benchmark_returns table.

    Returns:
        Polars Schema object describing the structure of the benchmark_returns table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('benchmark_returns')
    )