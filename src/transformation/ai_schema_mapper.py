import json

from langchain_ollama import ChatOllama

from src.transformation.schema_mapper import STANDARD_FIELDS


llm = ChatOllama(
    model="qwen3:4b",
    temperature=0
)


def ai_map_column(column_name: str) -> str | None:
    """
    Ask the local LLM to map an unknown source column
    to one of the supported standard financial fields.
    """

    standard_fields = list(STANDARD_FIELDS.keys())

    prompt = f"""
You are a data engineering schema mapping assistant.

Map the source column to exactly one of these standard fields:

{standard_fields}

Source column:
{column_name}

Return ONLY valid JSON in this format:

{{"mapped_field": "field_name"}}

If the column does not clearly match any standard field,
return:

{{"mapped_field": null}}

Do not provide explanations.
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    try:
        result = json.loads(content)
        mapped_field = result.get("mapped_field")

        if mapped_field in standard_fields:
            return mapped_field

    except json.JSONDecodeError:
        pass

    return None