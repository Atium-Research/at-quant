import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_factor_loadings(start: dt.date, end: dt.date) -> pl.DataFrame:
    """Load factor loading (exposure) data within a date range.

    Factor loadings represent each stock's sensitivity or exposure to various risk factors
    (e.g., size, value, momentum, industry). These are used in multi-factor risk models
    to decompose stock returns into systematic factor contributions and idiosyncratic returns.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.

    Returns:
        DataFrame containing factor loadings sorted by date, ticker, and factor.
        The 'year' column is dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('factor_loadings')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker', 'factor')
        )
    )

def get_factor_loadings_schema() -> pl.Schema:
    """Get the schema of the factor_loadings table.

    Returns:
        Polars Schema object describing the structure of the factor_loadings table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('factor_loadings')
    )
