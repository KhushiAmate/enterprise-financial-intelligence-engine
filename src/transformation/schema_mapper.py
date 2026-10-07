from difflib import SequenceMatcher


STANDARD_FIELDS = {
    "transaction_id": [
        "transaction_id",
        "transactionid",
        "transaction",
        "txn_id",
        "txn",
        "id",
    ],
    "vendor": [
        "vendor",
        "vendor_name",
        "supplier",
        "supplier_name",
        "merchant",
        "payee",
    ],
    "transaction_date": [
        "transaction_date",
        "transaction_dt",
        "date",
        "invoice_date",
        "invoice_dt",
        "purchase_date",
    ],
    "amount": [
        "amount",
        "total_amount",
        "total_cost",
        "cost",
        "expense",
        "expense_amount",
        "purchase_amount",
        "invoice_value",
        "net_value",
    ],
    "currency": [
        "currency",
        "currency_code",
        "curr",
    ],
    "department": [
        "department",
        "dept",
        "business_unit",
        "businessunit",
        "division",
    ],
    "category": [
        "category",
        "type",
        "expense_type",
        "spend_category",
    ],
}


def normalize_column_name(column_name: str) -> str:
    """Normalize a column name for comparison."""

    return (
        column_name.strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
    )


def similarity_score(value: str, candidate: str) -> float:
    """Return similarity between two strings."""

    return SequenceMatcher(
        None,
        value,
        candidate,
    ).ratio()


def map_column(column_name: str, threshold: float = 0.75) -> str | None:
    """
    Map an input column name to a standard financial field.

    Returns None when no sufficiently confident mapping exists.
    """

    normalized = normalize_column_name(column_name)

    # Exact/synonym match
    for standard_field, aliases in STANDARD_FIELDS.items():
        normalized_aliases = {
            normalize_column_name(alias)
            for alias in aliases
        }

        if normalized in normalized_aliases:
            return standard_field

    # Fuzzy match
    best_match = None
    best_score = 0.0

    for standard_field, aliases in STANDARD_FIELDS.items():
        for alias in aliases:
            score = similarity_score(
                normalized,
                normalize_column_name(alias),
            )

            if score > best_score:
                best_score = score
                best_match = standard_field

    if best_score >= threshold:
        return best_match

    return None


def map_columns(columns: list[str]) -> dict[str, str | None]:
    """Map multiple input columns to standard fields."""

    return {
        column: map_column(column)
        for column in columns
    }