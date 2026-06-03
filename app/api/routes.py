from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.factory import ai_service

router = APIRouter(prefix="/api", tags=["Chat"])

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Receives a user message and returns an AI-generated response.
    """
    try:
        ai_reply = await ai_service.generate_chat_response(request.message)
        return ChatResponse(reply=ai_reply)
    
    except Exception as e:
        # Global catch-all for service failures
        raise HTTPException(
            status_code=500, 
            detail=str(e)
        )
