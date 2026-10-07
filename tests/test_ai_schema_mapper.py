from src.transformation.ai_schema_mapper import ai_map_column


def test_ai_map_column():
    result = ai_map_column("supplier")

    assert result == "vendor"