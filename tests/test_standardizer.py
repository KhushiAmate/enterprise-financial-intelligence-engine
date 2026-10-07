import pandas as pd

from src.transformation.standardizer import standardize_dataframe


def test_standardize_dataframe():

    df = pd.DataFrame(
        {
            "supplier_name": ["AWS", "Microsoft"],
            "invoice_dt": ["2026-01-01", "2026-01-02"],
            "total_cost": [1000, 2000],
            "business_unit": ["Engineering", "Data"],
        }
    )

    mapping = {
        "supplier_name": "vendor",
        "invoice_dt": "transaction_date",
        "total_cost": "amount",
        "business_unit": "department",
    }

    result = standardize_dataframe(df, mapping)

    assert "vendor" in result.columns
    assert "transaction_date" in result.columns
    assert "amount" in result.columns
    assert "department" in result.columns

    assert "supplier_name" not in result.columns
    assert "total_cost" not in result.columns