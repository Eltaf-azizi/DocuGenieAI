<h1>DocuGenieAI</h1>

A Slack-integrated AI-powered chatbot built with Python, FastAPI, LlamaIndex, and Slack API to automate technical queries and assist developers by fetching accurate documentation answers in real time.


## 📚 Overview
This project is a hands-on learning experience that teaches you how to:

 - Build an AI chatbot for developer assistance.

 - Integrate with Slack to streamline communication.

 - Use LlamaIndex to query technical documentation.

 - Leverage tools like n8n for workflow automation.

 - Deploy using FastAPI for scalable and performant APIs.


## 🧠 Key Features
 - ✅ Slack integration with real-time chatbot responses.

 - ✅ Vector store support for document retrieval.

 - ✅ Modular Python structure for clarity and extensibility.

 - ✅ Workflow automation via n8n.

 - ✅ Easy-to-follow structure for beginners and intermediates.



## 📁 Project Structure
```bash
Copy
Edit
documentation/
│
├── storage/
│   ├── default_vector_store.json
│   ├── docstore.json
│   ├── graph_store.json
│   ├── image_vector_store.json
│   └── index_store.json
│
├── .env                # Environment variables for API keys and secrets
├── app.py              # Main FastAPI app logic
├── main.py             # Script to run the chatbot
├── README.md           # Project overview and usage
└── requirements.txt    # Python dependencies
```

## ⚙️ Installation
```bash
Copy
Edit
# Clone the repository
git clone https://github.com/yourusername/ai-docs-chatbot.git
cd ai-docs-chatbot

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```


## 🔑 Environment Variables
Create a .env file in the root directory with the following content:

```ini
Copy
Edit
SLACK_API_TOKEN=your_slack_token
OPENAI_API_KEY=your_openai_api_key
OTHER_CONFIG=...
```

## 🚀 Running the App
```bash
Copy
Edit
# Run the FastAPI server
python app.py
```
or

```bash
Copy
Edit
# Run the chatbot script
python main.py
```

## 🧪 Use Cases
 - Ask coding-related questions in Slack and get instant AI answers.

 - Integrate your company’s technical documentation.

 - Enhance team productivity with workflow automation (via n8n).

 - Scale with FastAPI's production-ready backend.

## 🧰 Tech Stack
 - Python

 - FastAPI

 - Slack API

 - LlamaIndex

 - n8n (for automation)

 - ChromaDB / JSON storage (for vector retrieval)


## 📘 Learning Goals
 - Learn how to use LlamaIndex with your documentation.

 - Understand Slackbot integration.

 - Automate common developer workflows.

 - Strengthen Python skills through real-world application.


## 📌 Future Improvements
 - Add support for multiple documentation sources.

 - Include natural language understanding improvements.

 - Dockerize for easy deployment.

 - Build a web UI interface for chatbot monitoring.


