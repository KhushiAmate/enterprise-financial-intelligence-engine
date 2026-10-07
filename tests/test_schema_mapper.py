from src.transformation.schema_mapper import map_columns


def test_schema_mapping():

    columns = [
        "supplier_name",
        "invoice_dt",
        "total_cost",
        "business_unit",
    ]

    mapping = map_columns(columns)

    assert mapping["supplier_name"] == "vendor"
    assert mapping["invoice_dt"] == "transaction_date"
    assert mapping["total_cost"] == "amount"
    assert mapping["business_unit"] == "department"


def test_unknown_column():

    mapping = map_columns(
        ["random_business_column"]
    )

    assert mapping["random_business_column"] is None