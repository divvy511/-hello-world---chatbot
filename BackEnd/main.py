from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

API_KEY = "your_api_key"
URL = "any_llm_endpoint" #For example: Groq,Openai,Togetherai etc

client = OpenAI(api_key=API_KEY, base_url=URL)


class Chat(BaseModel):
    user_input: str


@app.post("/chat")
def chat(request: Chat):
    try:
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a info chatbot. Answer crisp and precise",
                },
                {"role": "user", "content": request.user_input},
            ],
        )

        # Try accessing content safely
        content = response.choices[0].message.content
        return {"response": content}

    except Exception as e:
        print("Error occurred:", e)
        return {"error": str(e)}
