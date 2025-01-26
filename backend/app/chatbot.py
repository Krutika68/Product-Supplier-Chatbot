from langgraph import LangGraph
from .database import get_product_data
from transformers import pipeline

# Initialize LLM summarizer (HuggingFace GPT-2)
summarizer = pipeline("summarization", model="gpt2")

def summarize_product_data(data: str) -> str:
    """Summarize the product data using the LLM"""
    return summarizer(data)[0]['summary_text']

def process_query(query: str) -> str:
    # LangGraph node structure
    graph = LangGraph()
    graph.add_node("query_data", get_product_data)
    graph.add_node("summarize_data", summarize_product_data)
    
    # Run the LangGraph workflow
    result = graph.run(query)
    return result

async def get_chatbot_response(query: str) -> str:
    response = process_query(query)
    return response
