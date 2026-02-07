import datetime as dt

import bear_lake as bl
import polars as pl

from at_data_tools.clients import get_bear_lake_client


def load_betas(start: dt.date, end: dt.date) -> pl.DataFrame:
    """Load stock beta coefficients within a date range.

    Beta measures a stock's sensitivity to market movements. A beta of 1 indicates the stock
    moves in line with the market, >1 indicates higher volatility, and <1 indicates lower volatility.
    Used in risk models and portfolio construction.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.

    Returns:
        DataFrame containing beta coefficients sorted by date and ticker.
        The 'year' column is dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('betas')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )

def get_betas_schema() -> pl.Schema:
    """Get the schema of the betas table.

    Returns:
        Polars Schema object describing the structure of the betas table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('betas')
    )
