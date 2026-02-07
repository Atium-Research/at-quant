import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_scores(start: dt.date, end: dt.date, signals: list[str]) -> pl.DataFrame:
    """Load signal scores for specified signals within a date range.

    Scores represent normalized or standardized signal values, typically cross-sectionally
    ranked or z-scored. These are intermediate values used in the alpha generation pipeline,
    transforming raw signals into tradeable scores.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.
        signals: List of signal names to filter by.

    Returns:
        DataFrame containing scores sorted by date, ticker, and signal.
        The 'year' column is dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('scores')
            .filter(
                pl.col('date').is_between(start, end),
                pl.col('signal').is_in(signals)
            )
            .drop('year')
            .sort('date', 'ticker', 'signal')
        )
    )

def get_scores_schema() -> pl.Schema:
    """Get the schema of the scores table.

    Returns:
        Polars Schema object describing the structure of the scores table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('scores')
    )
