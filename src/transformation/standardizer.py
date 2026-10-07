from typing import Any

import pandas as pd


def standardize_dataframe(
    df: pd.DataFrame,
    mapping: dict[str, str | None],
) -> pd.DataFrame:
    """
    Rename columns using the provided schema mapping.

    Only columns with a valid mapping are renamed.
    Unmapped columns are preserved.
    """

    rename_mapping: dict[str, str] = {
        source: target
        for source, target in mapping.items()
        if target is not None
    }

    standardized_df = df.rename(columns=rename_mapping)

    return standardized_df