from app.tools.expense_tools import (
    get_total_expense,
    get_total_income,
    get_top_expense_category,
    get_top_income_category,
    get_recent_transactions,
    get_category_spending
)

TOOL_MAP = {
    "get_total_expense": get_total_expense,
    "get_total_income": get_total_income,
    "get_top_expense_category": get_top_expense_category,
    "get_top_income_category": get_top_income_category,
    "get_recent_transactions": get_recent_transactions,
    "get_category_spending": get_category_spending,
}


async def execute_tool(tool_name: str, arguments: dict):
    tool = TOOL_MAP.get(tool_name)

    if not tool:
        raise ValueError(f"Unknown tool: {tool_name}")

    return await tool(**arguments)
