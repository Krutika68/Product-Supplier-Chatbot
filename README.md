# AI-Powered Chatbot for Supplier and Product Information

## Overview
This project implements an AI-powered chatbot that allows users to query a product and supplier database using natural language. The chatbot fetches relevant data from a MySQL/PostgreSQL database and enhances responses with the help of a language model for summarization and contextual understanding. It also supports features like product comparisons, user preferences, and an analytics dashboard.


## Frontend (React) 

### Features:
- **Responsive UI**: Built with React and Material UI or Tailwind CSS for a smooth and modern user experience.
- **User Interaction**: A text input field to enter queries and receive chatbot responses.
- **Conversation History**: Displays the history of recent queries and responses.
- **State Management**: Utilizes Redux or Context API for managing state across components.
- **API Integration**: Axios is used for API calls to interact with the backend.

### Technologies Used:
- React.js
- Material UI / Tailwind CSS
- Axios
- Redux / Context API

## Backend (Python & LangGraph)

### Features:
- **LangGraph Integration**: Uses LangGraph for managing agent workflows and orchestrating tasks based on user queries.
- **LLM Summarization**: Open-source LLM (e.g., Hugging Face's GPT-2, GPT-3, or LLaMA 2) is used to summarize product and supplier data.
- **Database Interaction**: Python-based FastAPI or Flask handles requests to retrieve data from the MySQL/PostgreSQL database.

### Technologies Used:
- Python (FastAPI / Flask)
- LangGraph
- Open-source LLM (Hugging Face GPT-2, GPT-3, or LLaMA 2)

## Database (MySQL/PostgreSQL)

### Schema Design:
- **Products**: 
  - ID (Primary Key)
  - Name
  - Brand
  - Price
  - Category
  - Description
  - Supplier ID (Foreign Key)
  
- **Suppliers**: 
  - ID (Primary Key)
  - Name
  - Contact Info
  - Product Categories Offered

### Data Population:
- Populate the database with sample data of products and suppliers.

### Technologies Used:
- MySQL / PostgreSQL

## Functional Requirements
- **Query Examples**:
  - "Show me all products under brand X."
  - "Which suppliers provide laptops?"
  - "Give me details of product ABC."

### Features:
- **Data Retrieval**: The chatbot should fetch relevant data from the database.
- **LLM Enhancement**: The response should be enhanced using context from an LLM.
- **Structured Response**: Return responses with structured data for products and suppliers.
- **Error Handling**: Handle missing or incorrect queries gracefully.

## Technical Requirements

### Backend:
- Python (FastAPI or Flask)
- LangGraph for chatbot workflow
- Open-source LLM (Hugging Face GPT-2, GPT-3, LLaMA 2)
  
### Frontend:
- React with Material UI / Tailwind CSS
- Axios for API calls
- Redux / Context API for state management

### Database:
- MySQL/PostgreSQL

## Installation

### Clone the Repository
1. git clone https://github.com/yourusername/product-supplier-chatbot.git
2. cd product-supplier-chatbot 

### Backend Setup
1. Create a virtual environment : [python -m venv venv]

2. Activate the virtual environment : [venv\Scripts\activate]

3. Install the dependencies: [pip install -r backend/requirements.txt]

4. Set up the database (MySQL/PostgreSQL) and populate it with sample data.

5. Run the backend server : [uvicorn backend.app.main:app --reload]

### Frontend Setup
1. Navigate to the frontend directory : [cd frontend]

2. Install dependencies : [npm install]

3. Start the development server : [npm start]

*** The frontend will be running on http://localhost:3000 and the backend on http://127.0.0.1:8000.

### Usage
1. Open the web interface in the browser.
2. Enter queries in the input field, such as "Show me all products under brand X."
3. The chatbot will respond with relevant information fetched from the database, enhanced with LLM summaries.
