from src.ingestion.file_reader import read_file


def test_read_csv():
    df = read_file("data/raw/financial_transactions.csv")

    assert not df.empty
    assert len(df.columns) == 7
    assert "vendor" in df.columns
    assert "amount" in df.columns