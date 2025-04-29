# Hello World Chatbot 🤖

A simple chatbot using **FastAPI** as the backend and **Streamlit** as the frontend.

---

## 🚀 Getting Started

### 📋 Prerequisites
- Python 3.8+
- Install dependencies:
  ```bash
  pip install -r requirements.txt


### 🔧 Backend (FastAPI)

      cd backend    
      uvicorn main:app --reload


### 💻 Frontend (Streamlit)

      cd backend    
      uvicorn main:app --reload
    

📂 Project Structure
--------------------
    hello-chatbot/
    ├── backend/
    │   └── main.py              # FastAPI backend logic
    ├── frontend/
    │   └── app.py               # Streamlit UI implementation
    ├── requirements.txt         # Dependency list
    └── README.md                # Project documentation

🌐 API Documentation
--------------------

### POST /chat

**Request Format**Send user input as JSON:

    {"message": "Hello!"}   

**Response Format**Receive chatbot reply as JSON:

    {"response": "Hi! How can I help you?"} 

🔑 Important Notes
------------------

1.  **Backend First**: Always start the FastAPI backend before launching the Streamlit frontend.
    
2.  **Streaming**: Enabled via stream=True in both backend and frontend code.
    
3.  **Dependencies**: Ensure all packages in requirements.txt are installed.
    

Built using Python, FastAPI, and Streamlit.
