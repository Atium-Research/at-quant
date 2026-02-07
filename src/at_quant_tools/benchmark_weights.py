import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_benchmark_weights(start: dt.date, end: dt.date) -> pl.DataFrame:
    """Load benchmark portfolio weights within a date range.

    Benchmark weights represent the allocation of stocks in a benchmark index or portfolio,
    typically expressed as a percentage or proportion of the total portfolio value.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.

    Returns:
        DataFrame containing benchmark weights sorted by date and ticker.
        The 'year' column is dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('benchmark_weights')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )

def get_benchmark_weights_schema() -> pl.Schema:
    """Get the schema of the benchmark_weights table.

    Returns:
        Polars Schema object describing the structure of the benchmark_weights table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('benchmark_weights')
    )
