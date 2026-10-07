from pathlib import Path

import pandas as pd


SUPPORTED_FORMATS = {
    ".csv",
    ".json",
    ".parquet",
    ".xlsx",
    ".xls",
}


def read_file(file_path: str) -> pd.DataFrame:
    """
    Read a supported data file into a pandas DataFrame.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    if extension == ".csv":
        return pd.read_csv(path)

    if extension == ".json":
        return pd.read_json(path)

    if extension == ".parquet":
        return pd.read_parquet(path)

    if extension in {".xlsx", ".xls"}:
        return pd.read_excel(path)

    raise ValueError(
        f"Unsupported file format: {extension}. "
        f"Supported formats: {sorted(SUPPORTED_FORMATS)}"
    )