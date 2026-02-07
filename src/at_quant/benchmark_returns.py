import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_benchmark_returns(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        get_bear_lake_client().query(
            bl.table('benchmark_returns')
            .filter(pl.col('date').is_between(start, end))
            .sort('date')
        )
    )

def get_benchmark_returns_schema() -> pl.Schema:
    return (
        get_bear_lake_client().get_schema('benchmark_returns')
    )