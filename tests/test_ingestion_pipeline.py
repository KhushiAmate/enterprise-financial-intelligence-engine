from src.ingestion.ingestion_pipeline import process_file


def test_process_file():
    result = process_file(
        "data/raw/financial_transactions.csv"
    )

    assert "original_dataframe" in result
    assert "profile" in result
    assert "mapping" in result
    assert "standardized_dataframe" in result

    standardized_df = result["standardized_dataframe"]

    assert "vendor" in standardized_df.columns
    assert "amount" in standardized_df.columns
    assert "transaction_date" in standardized_df.columns