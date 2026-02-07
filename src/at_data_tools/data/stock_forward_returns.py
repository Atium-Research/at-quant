import datetime as dt

import bear_lake as bl
import polars as pl

from at_data_tools.clients import get_bear_lake_client


def load_stock_forward_returns(start: dt.date, end: dt.date) -> pl.DataFrame:
    """Load stock forward return data within a date range.

    Stock forward returns represent the next period's return for each stock,
    computed by shifting the return data forward by one period. This is essential
    for supervised learning models where you need to predict future returns based
    on current features.

    Args:
        start: Start date (inclusive) for the data range.
        end: End date (inclusive) for the data range.

    Returns:
        DataFrame containing stock forward returns sorted by date and ticker.
        The 'year' and 'return' columns are dropped from the results.
    """
    return (
        get_bear_lake_client().query(
            bl.table('stock_returns')
            .sort('ticker', 'date')
            .with_columns(
                pl.col('return')
                .shift(-1)
                .over('ticker')
                .alias('forward_return')
            )
            .filter(pl.col('date').is_between(start, end))
            .drop('year', 'return')
            .sort('date', 'ticker')
        )
    )

def get_stock_forward_returns_schema() -> pl.Schema:
    """Get the schema of the stock_forward_returns data.

    Returns:
        Polars Schema object describing the structure of the stock_forward_returns data,
        including column names and data types.
    """
    return pl.Schema({
        'date': pl.Date,
        'ticker': pl.String,
        'forward_return': pl.Float64
    })
