from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.factory import ai_service
from app.db.mongo import messages_collection
from app.services.appwrite_service import appwrite_service
from app.tools.expense_tools import (
    get_total_spent_this_month,
    get_top_expense_categories,
    get_recent_transactions,
)


router = APIRouter(prefix="/api", tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        await messages_collection.insert_one({
            "user_id": request.user_id,
            "content": request.message,
            "role": "user",
            "created_at": datetime.utcnow()
        })
        ai_reply = await ai_service.generate_chat_response(request.user_id, request.message)
        await messages_collection.insert_one({
            "user_id": request.user_id,
            "content": ai_reply,
            "role": "assistant",
            "created_at": datetime.utcnow()
        })
        return ChatResponse(reply=ai_reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/chat/{user_id}")
async def get_chat_history(user_id: str):
    # print( await get_total_spent_this_month(user_id))
    # print( await get_top_expense_categories(user_id))
    # print( await get_recent_transactions(user_id))
    messages = await messages_collection.find(
        {"user_id": user_id}
    ).sort("created_at", 1).to_list(100)
    for message in messages:
        message["_id"] = str(message["_id"])
    
    return messages