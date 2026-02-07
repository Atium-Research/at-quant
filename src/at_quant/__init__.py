from at_quant.clients import get_bear_lake_client
import polars as pl
import bear_lake as bl
import datetime as dt

bear_lake_client = get_bear_lake_client()


def load_alphas(start: dt.date, end: dt.date, signals: list[str]) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('alphas')
            .filter(
                pl.col('date').is_between(start, end),
                pl.col('signal').is_in(signals)
            )
            .drop('year')
            .sort('date', 'ticker', 'signal')
        )
    )


def load_benchmark_returns(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('benchmark_returns')
            .filter(pl.col('date').is_between(start, end))
            .sort('date')
        )
    )


def load_benchmark_weights(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('benchmark_weights')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )


def load_betas(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('betas')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )


def load_calendar(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('calendar')
            .filter(pl.col('date').is_between(start, end))
            .sort('date')
        )
    )


def load_etf_prices(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('etf_prices')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )


def load_etf_returns(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('etf_returns')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )


def load_factor_covariances(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('factor_covariances')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'factor_1', 'factor_2')
        )
    )


def load_factor_loadings(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('factor_loadings')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker', 'factor')
        )
    )


def load_idio_vol(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('idio_vol')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )


def load_scores(start: dt.date, end: dt.date, signals: list[str]) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('scores')
            .filter(
                pl.col('date').is_between(start, end),
                pl.col('signal').is_in(signals)
            )
            .drop('year')
            .sort('date', 'ticker', 'signal')
        )
    )


def load_signals(start: dt.date, end: dt.date, signals: list[str]) -> pl.DataFrame:
    return (
        bear_lake_client
        .query(
            bl.table('signals')
            .filter(
                pl.col('date').is_between(start, end),
                pl.col('signal').is_in(signals)
            )
            .drop('year')
            .sort('date', 'ticker', 'signal')
        )
    )


def load_stock_prices(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('stock_prices')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )


def load_stock_returns(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('stock_returns')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )


def load_universe(start: dt.date, end: dt.date) -> pl.DataFrame:
    return (
        bear_lake_client.query(
            bl.table('universe')
            .filter(pl.col('date').is_between(start, end))
            .drop('year')
            .sort('date', 'ticker')
        )
    )
