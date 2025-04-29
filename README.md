# Hello World Chatbot 🤖

A simple chatbot using **FastAPI** as the backend and **Streamlit** as the frontend.

## 📦 How to Run


### 🔧 Backend (FastAPI)

1.  bashCopyDownloadcd backend
    
2.  bashCopyDownloaduvicorn main:app --reload
    

### 💻 Frontend (Streamlit)

1.  bashCopyDownloadcd frontend
    
2.  bashCopyDownloadstreamlit run app.py
    

📂 Project Structure
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   hello-chatbot/  ├── backend/  │   └── main.py              # FastAPI backend logic  ├── frontend/  │   └── app.py               # Streamlit UI implementation  ├── requirements.txt         # Dependency list  └── README.md                # Project documentation   `

🌐 API Documentation
--------------------

### POST /chat

**Request Format**Send user input as JSON:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {"message": "Hello!"}   `

**Response Format**Receive chatbot reply as JSON:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {"response": "Hi! How can I help you?"}   `

🔑 Important Notes
------------------

1.  **Backend First**: Always start the FastAPI backend before launching the Streamlit frontend.
    
2.  pythonCopyDownloadAPI\_KEY = "your-actual-api-key-here"
    
3.  **Streaming**: Enabled via stream=True in both backend and frontend code.
    
4.  **Dependencies**: Ensure all packages in requirements.txt are installed.
    

Built with ❤️ using Python, FastAPI, and Streamlit.
