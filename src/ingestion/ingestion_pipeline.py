from src.ingestion.file_reader import read_file
from src.profiling.schema_profiler import profile_dataframe
from src.transformation.schema_mapper import map_columns
from src.transformation.standardizer import standardize_dataframe
from src.transformation.ai_schema_mapper import ai_map_columns


def process_file(file_path: str):
    """
    Read, profile, map, and standardize an input file.

    Deterministic mapping is attempted first.
    AI mapping is used only for unknown columns.
    """

    # 1. Read input file
    df = read_file(file_path)

    # 2. Profile schema
    profile = profile_dataframe(df)

    # 3. Deterministic mapping
    mapping = map_columns(list(df.columns))

    # 4. AI fallback for unknown columns
    unmapped_columns = [
        column
        for column, mapped_field in mapping.items()
        if mapped_field is None
    ]

    if unmapped_columns:
        ai_mapping = ai_map_columns(unmapped_columns)
        mapping.update(ai_mapping)

    # 5. Standardize dataframe
    standardized_df = standardize_dataframe(df, mapping)

    return {
        "original_dataframe": df,
        "profile": profile,
        "mapping": mapping,
        "standardized_dataframe": standardized_df,
    }