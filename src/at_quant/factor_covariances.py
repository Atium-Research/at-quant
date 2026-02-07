import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_factor_covariances(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        get_bear_lake_client().query(
            bl.table('factor_covariances')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'factor_1', 'factor_2')
        )
    )
