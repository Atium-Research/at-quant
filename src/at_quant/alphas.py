import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_alphas(start: dt.date, end: dt.date, signals: list[str]) -> pl.DataFrame:
    """Load alpha values for specified signals within a date range.

    Alpha values represent the expected excess return of a stock given a particular signal.
    This function retrieves alpha data from the bear_lake database, filtered by date range
    and signal names.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.
        signals: List of signal names to filter by.

    Returns:
        DataFrame containing alpha values sorted by date, ticker, and signal.
        The 'year' column is dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('alphas')
            .filter(
                pl.col('date').is_between(start, end),
                pl.col('signal').is_in(signals)
            )
            .drop('year')
            .sort('date', 'ticker', 'signal')
        )
    )

def get_alphas_schema() -> pl.Schema:
    """Get the schema of the alphas table.

    Returns:
        Polars Schema object describing the structure of the alphas table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('alphas')
    )