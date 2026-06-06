from app.db.mongo import messages_collection

async def get_recent_messages(user_id: str, limit=10):
    messages = await messages_collection.find(
        {
            "user_id": user_id
        }
    ).sort("created_at", 1).limit(limit).to_list(limit)

    history_messages = [
        {
            "role": msg["role"],
            "content": msg["content"]
        }
        for msg in messages
    ]

    return history_messages