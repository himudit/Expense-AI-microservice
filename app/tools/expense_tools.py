from app.services.appwrite_service import appwrite_service
from datetime import datetime


async def get_total_expense(
    user_id: str, start_date: str | None = None, end_date: str | None = None
):
    expenses = await appwrite_service.get_user_expenses(
        user_id=user_id, start_date=start_date, end_date=end_date
    )

    total_amount = sum(expense.data["ExpenseAmount"] for expense in expenses)

    return {"total_spent": total_amount}


async def get_total_income(
    user_id: str, start_date: str | None = None, end_date: str | None = None
):
    incomes = await appwrite_service.get_user_incomes(
        user_id=user_id, start_date=start_date, end_date=end_date
    )

    total_income = sum(income.data["IncomeAmount"] for income in incomes)

    return {"total_income": total_income}


async def get_top_expense_category(
    user_id: str, start_date: str | None = None, end_date: str | None = None
):
    expenses = await appwrite_service.get_user_expenses(
        user_id=user_id, start_date=start_date, end_date=end_date
    )

    categories = {}

    for expense in expenses:
        category = expense.data["Category"]
        amount = expense.data["ExpenseAmount"]

        categories[category] = categories.get(category, 0) + amount

    if not categories:
        return {"top_category": None, "amount": 0}

    top_category = max(categories, key=categories.get)

    return {"top_category": top_category, "amount": categories[top_category]}


async def get_top_income_category(
    user_id: str, start_date: str | None = None, end_date: str | None = None
):
    incomes = await appwrite_service.get_user_incomes(
        user_id=user_id, start_date=start_date, end_date=end_date
    )

    categories = {}

    for income in incomes:
        category = income.data["Category"]
        amount = income.data["IncomeAmount"]

        categories[category] = categories.get(category, 0) + amount

    if not categories:
        return {"top_category": None, "amount": 0}

    top_category = max(categories, key=categories.get)

    return {"top_category": top_category, "amount": categories[top_category]}


async def get_recent_transactions(user_id: str, limit: int = 10):
    """
    Returns recent transactions.
    """
    transactions = await appwrite_service.get_recent_transactions(user_id, limit=limit)
    result = []
    for t in transactions:
        created_at = (
            t.createdat if isinstance(t.createdat, str) else t.createdat.isoformat()
        )
        result.append(
            {
                "date": created_at,
                "type": t.data.get("Type"),  # "expense" or "income"
                "category": t.data.get("Category"),
                "amount": t.data.get("ExpenseAmount"),
                "note": t.data.get("Note"),
            }
        )

    return {"transactions": result}
