from app.services.appwrite_service import appwrite_service

async def get_total_spent_this_month(user_id: str):
    """
    Returns total expenses for current month.
    """
    expenses = await appwrite_service.get_user_expenses(user_id)

    # Calculate total

    return {
        "total_spent": 0
    }


async def get_top_expense_categories(user_id: str):
    """
    Returns highest spending categories.
    """
    expenses = await appwrite_service.get_user_expenses(user_id)

    return {
        "top_categories": []
    }


async def get_recent_transactions(user_id: str):
    """
    Returns recent transactions.
    """
    transactions = await appwrite_service.get_recent_transactions(user_id)

    return {
        "transactions": transactions
    }