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

