from appwrite.query import Query

from app.db.appwrite import databases
from app.config import settings


class AppwriteService:

    async def get_user_expenses(
        self,
        user_id: str
    ):
        response = databases.list_documents(
            database_id=settings.APPWRITE_DATABASE_ID,
            collection_id=settings.APPWRITE_COLLECTION2_ID,
            queries=[   
                Query.equal("userid", user_id)
            ]
        )

        return response.documents

    async def get_user_incomes(
        self,
        user_id: str
    ):
        response = databases.list_documents(
            database_id=settings.APPWRITE_DATABASE_ID,
            collection_id=settings.APPWRITE_COLLECTION5_ID,
            queries=[
                Query.equal("userid", user_id)
            ]
        )

        return response.documents

    async def get_recent_transactions(
        self,
        user_id: str,
        limit: int = 10
    ):
        expenses = databases.list_documents(
            database_id=settings.APPWRITE_DATABASE_ID,
            collection_id=settings.APPWRITE_COLLECTION2_ID,
            queries=[
                Query.equal("userid", user_id),
                Query.order_desc("$createdAt"),
                Query.limit(limit)
            ]
        )

        incomes = databases.list_documents(
            database_id=settings.APPWRITE_DATABASE_ID,
            collection_id=settings.APPWRITE_COLLECTION5_ID,
            queries=[
                Query.equal("userid", user_id),
                Query.order_desc("$createdAt"),
                Query.limit(limit)
            ]
        )

        transactions = (
            expenses.documents
            + incomes.documents
        )

        transactions.sort(
            key=lambda x: x.createdat,
            reverse=True
        )

        return transactions[:limit]

    async def get_user_profile(
        self,
        user_id: str
    ):
        response = databases.list_documents(
            database_id=settings.APPWRITE_DATABASE_ID,
            collection_id=settings.APPWRITE_COLLECTION3_ID,
            queries=[
                Query.equal("userid", user_id)
            ]
        )

        documents = response.documents

        return documents[0] if documents else None


appwrite_service = AppwriteService()