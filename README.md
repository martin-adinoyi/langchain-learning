# LangChain Learning

Hands-on practice learning LangChain, with LangSmith and LangGraph to follow.

## Current project

`langchain-groq-practice.py` is a multi-turn terminal chat app built with LangChain and Groq. It uses a prompt template, in-memory chat history, and the `openai/gpt-oss-20b` model.

## Setup

1. Install [uv](https://docs.astral.sh/uv/).
2. Clone the repo and install dependencies:
   ```bash
   git clone https://github.com/<your-username>/langchain-learning.git
   cd langchain-learning
   uv sync
   ```
3. Create a `.env` file (see `.env.example`) and add your key from [Groq](https://console.groq.com):
   ```
   GROQ_API_KEY=your_key_here
   ```

## Run

```bash
uv run langchain-groq-practice.py
```

Type `exit` or `quit` to end the chat.

## Author

Martin Adinoyi: [LinkedIn](https://www.linkedin.com/in/martin-adinoyi)