# 🤖 AI Teaching Assistant

A simple Streamlit-based web app that answers educational questions using Groq's LLM API (with Hugging Face as a fallback option).

## Features
- Ask any question and get an AI-generated, insightful answer
- Conversation history with a clean, styled UI
- Export chat history as a `.txt` file
- Clear conversation with one click
- Dark theme UI

## Tech Stack
- Python
- Streamlit
- Groq API (LLaMA 3.1 / Mixtral models)

## Setup

1. Clone the repository
```bash
git clone https://github.com/saniya-s4/AI-Teaching-assistant.git
cd AI-Teaching-assistant
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Add your Groq API key in a `.env` file
```
GROQ_API_KEY=your_api_key_here
```

4. Run the app
```bash
streamlit run main.py
```

## Author
Made by [Saniya](https://github.com/saniya-s4)
