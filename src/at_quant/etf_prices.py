import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_etf_prices(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        get_bear_lake_client().query(
            bl.table('etf_prices')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )

def get_etf_prices_schema() -> pl.Schema:
    return (
        get_bear_lake_client().get_schema('etf_prices')
    )
