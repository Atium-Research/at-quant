import polars as pl
import numpy as np

def build_covariance_matrix(
        tickers: pl.DataFrame,
        factor_loadings: pl.DataFrame, 
        factor_covariances: pl.DataFrame, 
        idio_vol: pl.DataFrame
    ) -> pl.DataFrame:
    factor_loadings_np = (
        factor_loadings
        .filter(pl.col('ticker').is_in(tickers))
        .sort('ticker', 'factor')
        .pivot(index='ticker', on='factor', values='loading')
        .drop('ticker')
        .to_numpy()
    )

    factor_covariances_np = (
        factor_covariances
        .sort('factor_1', 'factor_2')
        .pivot(index='factor_1', on='factor_2', values='covariance')
        .drop('factor_1')
        .to_numpy()
    )

    idio_vol_np = np.diag(
        idio_vol
        .filter(pl.col('ticker').is_in(tickers))
        .select('ticker', 'idio_vol')
        .sort('ticker')
        ['idio_vol']
    )

    covariance_matrix_np = factor_loadings_np @ factor_covariances_np @ factor_loadings_np.T + idio_vol_np ** 2
    covariance_matrix = pl.from_numpy(covariance_matrix_np)
    covariance_matrix.columns = tickers
    covariance_matrix = (
        covariance_matrix
        .with_columns(
            pl.Series(tickers).alias('ticker')
        )
        .select('ticker', *tickers)
    )
    
    return covariance_matrix