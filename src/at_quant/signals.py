import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_signals(start: dt.date, end: dt.date, signals: list[str]) -> pl.DataFrame:
    """Load raw signal values for specified signals within a date range.

    Signals are raw quantitative indicators derived from fundamental, technical, or
    alternative data. These represent the initial stage of the alpha generation pipeline
    before normalization and combination into alphas.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.
        signals: List of signal names to filter by.

    Returns:
        DataFrame containing signal values sorted by date, ticker, and signal.
        The 'year' column is dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('signals')
            .filter(
                pl.col('date').is_between(start, end),
                pl.col('signal').is_in(signals)
            )
            .drop('year')
            .sort('date', 'ticker', 'signal')
        )
    )

def get_signals_schema() -> pl.Schema:
    """Get the schema of the signals table.

    Returns:
        Polars Schema object describing the structure of the signals table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('signals')
    )
