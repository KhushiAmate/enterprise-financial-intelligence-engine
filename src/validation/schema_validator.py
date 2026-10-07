from typing import Any

import pandas as pd


STANDARD_SCHEMA = {
    "transaction_id": "string",
    "vendor": "string",
    "transaction_date": "date",
    "amount": "numeric",
    "currency": "string",
    "department": "string",
    "category": "string",
}


def validate_dataframe(df: pd.DataFrame) -> dict[str, Any]:
    """
    Validate a standardized financial DataFrame.
    """

    errors: list[str] = []
    warnings: list[str] = []

    # Check required fields
    required_fields = [
        "vendor",
        "amount",
    ]

    for field in required_fields:
        if field not in df.columns:
            errors.append(
                f"Missing required field: {field}"
            )

    # Validate amount
    if "amount" in df.columns:
        if not pd.api.types.is_numeric_dtype(df["amount"]):
            errors.append(
                "Field 'amount' must be numeric"
            )

    # Validate transaction date if present
    if "transaction_date" in df.columns:
        converted_dates = pd.to_datetime(
            df["transaction_date"],
            errors="coerce",
        )

        invalid_dates = converted_dates.isna().sum()

        if invalid_dates > 0:
            errors.append(
                f"Field 'transaction_date' contains "
                f"{invalid_dates} invalid date values"
            )

    # Check completely empty columns
    for column in df.columns:
        if df[column].isna().all():
            warnings.append(
                f"Column '{column}' contains only null values"
            )

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }