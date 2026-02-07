import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_calendar(start: dt.date, end: dt.date) -> pl.DataFrame:
    """Load trading calendar data within a date range.

    The trading calendar contains information about market trading days, including
    trading dates, holidays, and other calendar-related metadata used for
    time-series alignment and trading day calculations.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.

    Returns:
        DataFrame containing calendar data sorted by date.
    """
    return (
        get_bear_lake_client().query(
            bl.table('calendar')
            .filter(pl.col('date').is_between(start, end))
            .sort('date')
        )
    )

def get_calendar_schema() -> pl.Schema:
    """Get the schema of the calendar table.

    Returns:
        Polars Schema object describing the structure of the calendar table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('calendar')
    )
