import os
from functools import lru_cache

import bear_lake as bl
from dotenv import load_dotenv


@lru_cache(maxsize=1)
def get_bear_lake_client() -> bl.Database:
    load_dotenv(override=True)

    storage_options = {
        "aws_access_key_id": os.getenv("ACCESS_KEY_ID"),
        "aws_secret_access_key": os.getenv("SECRET_ACCESS_KEY"),
        "region": os.getenv("REGION"),
        "endpoint_url": os.getenv("ENDPOINT"),
    }

    url = f"s3://{os.getenv('BUCKET')}"

    return bl.connect_s3(path=url, storage_options=storage_options)
