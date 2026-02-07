import os
from functools import lru_cache

import bear_lake as bl
from dotenv import load_dotenv


@lru_cache(maxsize=1)
def get_bear_lake_client() -> bl.Database:
    """Get a cached connection to the Bear Lake database stored in S3.

    This function creates and caches a connection to the Bear Lake database,
    which stores quantitative finance data in S3-compatible storage. The connection
    is configured using environment variables for AWS credentials and S3 endpoints.

    The function uses LRU caching to ensure only one connection is created and reused
    across the application, improving performance and resource utilization.

    Environment Variables Required:
        ACCESS_KEY_ID: AWS access key ID for S3 authentication.
        SECRET_ACCESS_KEY: AWS secret access key for S3 authentication.
        REGION: AWS region where the S3 bucket is located.
        ENDPOINT: S3 endpoint URL (useful for S3-compatible services).
        BUCKET: Name of the S3 bucket containing the Bear Lake data.

    Returns:
        A Bear Lake Database connection object that can be used to query tables.

    Note:
        Environment variables are loaded from a .env file using dotenv.
        The connection is cached, so subsequent calls return the same instance.
    """
    load_dotenv(override=True)

    storage_options = {
        "aws_access_key_id": os.getenv("ACCESS_KEY_ID"),
        "aws_secret_access_key": os.getenv("SECRET_ACCESS_KEY"),
        "region": os.getenv("REGION"),
        "endpoint_url": os.getenv("ENDPOINT"),
    }

    url = f"s3://{os.getenv('BUCKET')}"

    return bl.connect_s3(path=url, storage_options=storage_options)
