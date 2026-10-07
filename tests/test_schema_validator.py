import pandas as pd

from src.validation.schema_validator import validate_dataframe


def test_valid_dataframe():
    df = pd.DataFrame(
        {
            "vendor": ["AWS", "Microsoft"],
            "amount": [1000.0, 2000.0],
            "transaction_date": [
                "2026-01-01",
                "2026-01-02",
            ],
        }
    )

    result = validate_dataframe(df)

    assert result["valid"] is True
    assert result["errors"] == []


def test_missing_required_field():
    df = pd.DataFrame(
        {
            "vendor": ["AWS"],
        }
    )

    result = validate_dataframe(df)

    assert result["valid"] is False
    assert "Missing required field: amount" in result["errors"]


def test_invalid_amount():
    df = pd.DataFrame(
        {
            "vendor": ["AWS"],
            "amount": ["not-a-number"],
        }
    )

    result = validate_dataframe(df)

    assert result["valid"] is False
    assert "Field 'amount' must be numeric" in result["errors"]


def test_invalid_date():
    df = pd.DataFrame(
        {
            "vendor": ["AWS"],
            "amount": [1000.0],
            "transaction_date": ["not-a-date"],
        }
    )

    result = validate_dataframe(df)

    assert result["valid"] is False
    assert any(
        "invalid date values" in error
        for error in result["errors"]
    )