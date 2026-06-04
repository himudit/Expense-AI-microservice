from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

app = FastAPI(
    title="ExpenseMate AI Microservice",
    description="Backend AI service for ExpenseMate",
    version="1.0.0"
)

# Configure CORS for the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register our API routes
app.include_router(router)

@app.get("/")
async def health_check():
    return {"status": "healthy", "service": "ExpenseMate AI"}
