from src.transformation.ai_schema_mapper import ai_map_columns


def test_ai_map_columns():
    result = ai_map_columns(
        [
            "supplier",
            "invoice_total",
            "cost_center",
        ]
    )

    assert result["supplier"] == "vendor"
    assert result["invoice_total"] == "amount"
    assert result["cost_center"] == "department"