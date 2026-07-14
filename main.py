# main.py (Streamlit)
# Switch provider by changing the import line:
#from hf import generate_response
from groq import generate_response

import io
import streamlit as st

CSS = """
<style>
.history-wrap {max-height: 420px; overflow-y: auto; padding-right: 6px;}
.qa-card{
    border: 1px solid #2d3748;
    background: #1a1f2e;
    border-radius: 10px;
    padding: 14px 16px;
    margin: 10px 0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.3);
}
.q{font-weight: 700; color: #64b5f6; margin-bottom: 8px;}
.a{white-space: pre-wrap; color: #e0e0e0; line-height: 1.5;}
.stButton > button {background-color: #64b5f6; color: #fff;font-weight: 700; border: none; padding: 10px 32px; border-radius: 4px; cursor: pointer;}
h3{color: #64b5f6;}
.stTextInput > div > div > input {
    background-color: #1a1f2e;
    color: #FAFAFA;
    border: 1px solid #4A90D9;
    border-radius: 8px;
}
</style>
"""

def export_bytes(history):
    text = "".join([f"Q{i}: {h['question']}\nA{i}: {h['answer']}\n\n" for i, h in enumerate(history, 1)])
    return io.BytesIO(text.encode("utf-8"))

def setup_ui():
    st.set_page_config(page_title="AI Teaching Assistant", layout="centered")
    st.title("🤖 AI Teaching Assistant")
    st.write("Ask me anything about various subjects, and I'll provide an insightful answer.")
    st.session_state.setdefault("history", [])

    col_clear, col_export = st.columns([1, 2])
    with col_clear:
        if st.button("🧹 Clear Conversation"):
            st.session_state.history = []
            st.rerun()
    with col_export:
        if st.session_state.history:
            st.download_button(
                label="📤 Export Chat History",
                data=export_bytes(st.session_state.history),
                file_name="AI_Teaching_Assistant_Conversation.txt",
                mime="text/plain",
            )

    user_input = st.text_input("Enter your question here:")
    if st.button("Ask"):
        q = user_input.strip()
        if q:
            with st.spinner("Generating AI response..."):
                a = generate_response(q, temperature=0.3)
            st.session_state.history.insert(0, {"question": q, "answer": a})
            st.rerun()
        else:
            st.warning("⚠️ Please enter a question before clicking Ask.")

    st.markdown("### Conversation History")
    st.markdown(CSS, unsafe_allow_html=True)
    st.markdown("<style>.stApp {background-color: #0E1117; color: #FAFAFA;}</style>", unsafe_allow_html=True)

    cards = []
    for i, h in enumerate(st.session_state.history, 1):
        cards.append(f'<div class="qa-card"><div class="q">Q{i}: {h["question"]}</div><div class="a">{h["answer"]}</div></div>')
    st.markdown('<div class="history-wrap">' + "".join(cards) + "</div>", unsafe_allow_html=True)

def main():
    setup_ui()

if __name__ == "__main__":
    main()
