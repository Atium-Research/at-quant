import datetime as dt

import bear_lake as bl
import polars as pl

from at_data_tools.clients import get_bear_lake_client


def load_idio_vol(start: dt.date, end: dt.date) -> pl.DataFrame:
    """Load idiosyncratic volatility data within a date range.

    Idiosyncratic volatility (idio vol) represents the stock-specific risk that cannot
    be explained by systematic factors. It's the residual volatility after accounting
    for factor exposures in a multi-factor risk model. Used for risk management and
    portfolio construction.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.

    Returns:
        DataFrame containing idiosyncratic volatility sorted by date and ticker.
        The 'year' column is dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('idio_vol')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )

def get_idio_vol_schema() -> pl.Schema:
    """Get the schema of the idio_vol table.

    Returns:
        Polars Schema object describing the structure of the idio_vol table,
        including column names and data types.
    """
    return (
        get_bear_lake_client().get_schema('idio_vol')
    )
