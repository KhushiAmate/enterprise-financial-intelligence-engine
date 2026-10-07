import pandas as pd

from src.profiling.schema_profiler import profile_dataframe


def test_profile_dataframe():
    df = pd.DataFrame(
        {
            "vendor": ["AWS", "Microsoft", "AWS"],
            "amount": [1000.0, 2000.0, 1500.0],
            "transaction_date": pd.to_datetime(
                ["2026-01-01", "2026-01-02", "2026-01-03"]
            ),
            "region": ["US", "India", None],
        }
    )

    profile = profile_dataframe(df)

    assert len(profile) == 4

    profile_by_column = {
        item["column"]: item
        for item in profile
    }

    assert profile_by_column["vendor"]["detected_type"] == "string"
    assert profile_by_column["amount"]["detected_type"] == "numeric"
    assert profile_by_column["transaction_date"]["detected_type"] == "date"

    assert profile_by_column["region"]["nullable"] is True
    assert profile_by_column["region"]["null_count"] == 1