from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .chatbot import get_chatbot_response
from langgraph import LangGraph


app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/chat")
async def chat(request: QueryRequest):
    response = await get_chatbot_response(request.query)
    if not response:
        raise HTTPException(status_code=500, detail="Failed to process the query")
    return {"response": response}
