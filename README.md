# at-data-tools

Atium Research backtesting and research tools package for quantitative finance data access.

## Overview

`at-data-tools` is a Python library that provides convenient access to quantitative finance datasets stored in a Bear Lake database. It offers functions to load historical market data, alphas, betas, factor models, and other quantitative signals, all returned as Polars DataFrames for efficient data analysis.

## Installation

Install the package using pip:

```bash
pip install at-data-tools
```

Or with uv:

```bash
uv add at-data-tools
```

## Configuration

The package requires AWS credentials to access the S3-backed Bear Lake database. Create a `.env` file in your project root with the following variables:

```env
ACCESS_KEY_ID=your_aws_access_key
SECRET_ACCESS_KEY=your_aws_secret_key
REGION=your_aws_region
ENDPOINT=your_s3_endpoint_url
BUCKET=your_bucket_name
```

## Usage

### Basic Example

```python
import datetime as dt
import at_data_tools as adt

# Load stock prices for a date range
start = dt.date(2023, 1, 1)
end = dt.date(2023, 12, 31)
prices = adt.load_stock_prices(start, end)

# Load alphas for specific signals
signals = ['reversal']
alphas = adt.load_alphas(start, end, signals)

# View the schema of any table
schema = adt.get_stock_prices_schema()
print(schema)
```

## Available Data

### Market Data
- `load_stock_prices(start, end)` - Load historical stock prices
- `load_stock_returns(start, end)` - Load stock returns
- `load_etf_prices(start, end)` - Load ETF prices
- `load_etf_returns(start, end)` - Load ETF returns

### Alpha & Signals
- `load_alphas(start, end, signals)` - Load alpha values for specified signals
- `load_signals(start, end, signals)` - Load raw signal values
- `load_scores(start, end, signals)` - Load signal scores

### Risk Models
- `load_betas(start, end)` - Load market betas
- `load_factor_loadings(start, end)` - Load factor model loadings
- `load_factor_covariances(start, end)` - Load factor covariance matrices
- `load_idio_vol(start, end)` - Load idiosyncratic volatility

### Benchmarks
- `load_benchmark_weights(start, end)` - Load benchmark portfolio weights
- `load_benchmark_returns(start, end)` - Load benchmark returns

### Reference Data
- `load_universe(start, end)` - Load trading universe membership
- `load_calendar(start, end)` - Load trading calendar

### Schema Inspection

Each data loader has a corresponding schema function:
- `get_stock_prices_schema()` - Returns Polars schema for stock prices
- `get_alphas_schema()` - Returns Polars schema for alphas
- And similarly for all other data types...

## Data Types

All functions return `polars.DataFrame` objects for efficient data manipulation. Date parameters accept `datetime.date` objects.

## Requirements

- Python >= 3.13
- polars >= 1.38.1
- bear-lake >= 0.1.5
- python-dotenv >= 1.2.1

## License

Copyright Atium Research. All rights reserved.
