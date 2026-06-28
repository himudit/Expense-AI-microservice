import logging
import traceback

logger = logging.getLogger(__name__)

from app.services.appwrite_service import appwrite_service
from datetime import datetime


async def get_total_expense(
    user_id: str, start_date: str | None = None, end_date: str | None = None
):
    try:
        expenses = await appwrite_service.get_user_expenses(
            user_id=user_id, start_date=start_date, end_date=end_date
        )
        total_amount = sum(expense.data["ExpenseAmount"] for expense in expenses)
        return {"total_spent": total_amount}
    except Exception as e:
        logger.error(f"get_total_expense error: {e}", exc_info=True)
        raise


async def get_total_income(
    user_id: str, start_date: str | None = None, end_date: str | None = None
):
    try:
        incomes = await appwrite_service.get_user_incomes(
            user_id=user_id, start_date=start_date, end_date=end_date
        )
        total_income = sum(income.data["IncomeAmount"] for income in incomes)
        return {"total_income": total_income}
    except Exception as e:
        logger.error(f"get_total_income error: {e}", exc_info=True)
        raise


async def get_top_expense_category(
    user_id: str, start_date: str | None = None, end_date: str | None = None
):
    try:
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
    except Exception as e:
        logger.error(f"get_top_expense_category error: {e}", exc_info=True)
        raise


async def get_top_income_category(
    user_id: str, start_date: str | None = None, end_date: str | None = None
):
    try:
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
    except Exception as e:
        logger.error(f"get_top_income_category error: {e}", exc_info=True)
        raise


async def get_recent_transactions(user_id: str, limit: int = 10):
    try:
        transactions = await appwrite_service.get_recent_transactions(user_id, limit=limit)

        result = []
        for t in transactions:
            created_at = (
            t.createdat if isinstance(t.createdat, str) else t.createdat.isoformat()
            )

            income_amount = t.data.get("IncomeAmount")
            expense_amount = t.data.get("ExpenseAmount")

            if income_amount is not None:
                transaction_type = "Income"
                amount = income_amount
            else:
                transaction_type = "Expense"
                amount = expense_amount

            result.append(
                {
                    "date": created_at,
                    "type": transaction_type,
                    "category": t.data.get("Category"),
                    "amount": amount,
                    "note": t.data.get("Note"),
                }
            )

        return {"transactions": result}
    except Exception as e:
        logger.error(f"get_recent_transactions error: {e}", exc_info=True)
        raise


async def get_category_spending(
    user_id: str,
    category: str,
    start_date: str,
    end_date: str,
):
    try:
        expenses = await appwrite_service.get_user_expenses(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date,
        )
        total = 0
        for expense in expenses:
            if expense.data["Category"].lower() == category.lower():
                total += expense.data["ExpenseAmount"]

        return {
            "category": category,
            "total_spent": total,
            "start_date": start_date,
            "end_date": end_date,
        }
    except Exception as e:
        logger.error(f"get_category_spending error: {e}", exc_info=True)
        raise