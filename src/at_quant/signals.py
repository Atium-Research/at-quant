import datetime as dt

import bear_lake as bl
import polars as pl

from at_quant.clients import get_bear_lake_client


def load_signals(start: dt.date, end: dt.date, signals: list[str]) -> pl.DataFrame:
    return (
        get_bear_lake_client().query(
            bl.table('signals')
            .filter(
                pl.col('date').is_between(start, end),
                pl.col('signal').is_in(signals)
            )
            .drop('year')
            .sort('date', 'ticker', 'signal')
        )
    )
