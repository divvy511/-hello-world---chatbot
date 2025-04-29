# Hello World Chatbot 🤖

A simple chatbot using **FastAPI** as the backend and **Streamlit** as the frontend.

## 📦 How to Run

### 🔧 Backend (FastAPI)

```bash
cd backend
uvicorn main:app --reload

💻 Frontend (Streamlit)
bash
Copy
Edit
cd frontend
streamlit run app.py
📁 Project Structure
bash
Copy
Edit
hello-chatbot/
├── backend/
│   └── main.py              # FastAPI backend code
├── frontend/
│   └── app.py               # Streamlit frontend code
├── requirements.txt         # Python dependencies
└── README.md                # Project overview
✅ Requirements
Install dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
🌐 API Endpoint
POST /chat: Accepts user input and returns chatbot response as JSON:

json
Copy
Edit
{
  "response": "<bot reply>"
}
📌 Notes
Ensure your backend is running before launching the Streamlit app.

Replace API_KEY and model name in main.py with your actual values.

Streams are handled via stream=True in both backend and frontend.

Built with ❤️ using Python, FastAPI, and Streamlit.
