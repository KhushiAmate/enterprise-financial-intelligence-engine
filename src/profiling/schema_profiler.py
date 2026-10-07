from typing import Any

import pandas as pd


def profile_dataframe(df: pd.DataFrame) -> list[dict[str, Any]]:
    """
    Analyze a DataFrame and return metadata for every column.
    """

    profile = []

    for column in df.columns:
        series = df[column]

        if pd.api.types.is_numeric_dtype(series):
            detected_type = "numeric"

        elif pd.api.types.is_datetime64_any_dtype(series):
            detected_type = "date"

        elif pd.api.types.is_bool_dtype(series):
            detected_type = "boolean"

        else:
            detected_type = "string"

        profile.append(
            {
                "column": column,
                "detected_type": detected_type,
                "nullable": bool(series.isna().any()),
                "null_count": int(series.isna().sum()),
                "null_percentage": round(
                    float(series.isna().mean() * 100), 2
                ),
                "unique_count": int(series.nunique(dropna=True)),
            }
        )

    return profile