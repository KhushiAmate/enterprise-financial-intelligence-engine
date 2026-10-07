import json

from langchain_ollama import ChatOllama

from src.transformation.schema_mapper import STANDARD_FIELDS


llm = ChatOllama(
    model="qwen3:4b",
    temperature=0
)


def ai_map_columns(column_names: list[str]) -> dict[str, str | None]:
    """
    Map multiple unknown source columns to standard fields
    using a single LLM call.
    """

    if not column_names:
        return {}

    standard_fields = list(STANDARD_FIELDS.keys())

    prompt = f"""
You are a data engineering schema mapping assistant.

Map each source column to the most appropriate standard financial field.

Allowed standard fields:

{standard_fields}

Source columns:

{column_names}

Return ONLY valid JSON.

The JSON keys must be the source column names.
The values must be one of the allowed standard fields or null.

Example:

{{
    "supplier_name": "vendor",
    "invoice_total": "amount",
    "cost_center": "department",
    "random_column": null
}}

Do not provide explanations.
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    try:
        result = json.loads(content)
    except json.JSONDecodeError:
        return {column: None for column in column_names}

    validated_result = {}

    for column in column_names:
        mapped_field = result.get(column)

        if mapped_field in standard_fields:
            validated_result[column] = mapped_field
        else:
            validated_result[column] = None

    return validated_result