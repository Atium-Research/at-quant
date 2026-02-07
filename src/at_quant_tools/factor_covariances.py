import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_factor_covariances(start: dt.date, end: dt.date) -> pl.DataFrame:
    """Load factor covariance matrix data within a date range.

    Factor covariances measure how different risk factors move together, forming
    the covariance matrix used in multi-factor risk models. This is essential for
    portfolio risk calculation, optimization, and hedging strategies.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.

    Returns:
        DataFrame containing factor covariances sorted by date, factor_1, and factor_2.
        The 'year' column is dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('factor_covariances')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'factor_1', 'factor_2')
        )
    )

def get_factor_covariances_schema() -> pl.Schema:
    """Get the schema of the factor_covariances table.

    Returns:
        Polars Schema object describing the structure of the factor_covariances table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('factor_covariances')
    )
