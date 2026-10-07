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


def test_deterministic_mapping_does_not_need_ai(monkeypatch):
    def fail_if_called(_):
        raise AssertionError("AI should not be called")

    monkeypatch.setattr(
        "src.ingestion.ingestion_pipeline.ai_map_columns",
        fail_if_called,
    )

    result = process_file(
        "data/raw/financial_transactions.csv"
    )

    assert result["mapping"]["vendor"] == "vendor"
    assert result["mapping"]["amount"] == "amount"
    
def test_ai_mapping_for_unknown_column(monkeypatch, tmp_path):
    test_file = tmp_path / "unknown_schema.csv"

    test_file.write_text(
        "supplier_name,cost_center,total_cost\n"
        "AWS,Engineering,1000\n"
        "Microsoft,Data,2000\n"
    )

    def mock_ai_mapping(columns):
        assert "cost_center" in columns

        return {
            "cost_center": "department"
        }

    monkeypatch.setattr(
        "src.ingestion.ingestion_pipeline.ai_map_columns",
        mock_ai_mapping,
    )

    result = process_file(str(test_file))

    assert result["mapping"]["supplier_name"] == "vendor"
    assert result["mapping"]["total_cost"] == "amount"
    assert result["mapping"]["cost_center"] == "department"    