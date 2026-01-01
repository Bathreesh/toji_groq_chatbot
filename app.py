import streamlit as st
from langchain_groq import ChatGroq
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Toji • AI Chat",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

CUSTOM_CSS = """
<style>
.stApp {
    background: radial-gradient(circle at top, #111827 0, #020617 55%);
    color: #e5e7eb;
    font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Center content nicely on desktop, full on mobile */
.main .block-container {
    max-width: 720px;
    padding-top: 2.0rem;
    padding-bottom: 2.0rem;
}

/* Main title */
.toji-title {
    text-align: center;
    font-weight: 700;
    font-size: 2.0rem;
    margin-bottom: 0.0rem;
    background: linear-gradient(90deg, #22c55e, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle: line you mentioned */
.toji-subtitle {
    text-align: center;
    color: #9ca3af;
    font-size: 0.92rem;
    margin-top: 0.15rem;
    margin-bottom: 0.15rem;  /* change to 0 if you want no gap */
}

/* Chat container */
.chat-container {
    border-radius: 18px;
    padding: 0.9rem 0.8rem;
    background: rgba(15, 23, 42, 0.9);
    border: 1px solid rgba(55, 65, 81, 0.7);
    max-height: 65vh;
    overflow-y: auto;
}

/* Chat messages */
.toji-message {
    padding: 0.65rem 0.85rem;
    border-radius: 14px;
    margin-bottom: 0.35rem;
    font-size: 0.9rem;
    line-height: 1.4;
}

.toji-user {
    background: linear-gradient(135deg, #22c55e33, #22c55e11);
    border: 1px solid #22c55e55;
    margin-left: 2.5rem;
}

.toji-bot {
    background: linear-gradient(135deg, #111827, #020617);
    border: 1px solid #4b5563;
    margin-right: 2.5rem;
}

/* Tighter margins on phone */
@media (max-width: 768px) {
    .toji-user { margin-left: 1rem; }
    .toji-bot { margin-right: 1rem; }
}

/* Name labels */
.msg-header {
    font-size: 0.78rem;
    font-weight: 600;
    margin-bottom: 0.18rem;
    opacity: 0.9;
}

.msg-user-name { color: #22c55e; }
.msg-bot-name  { color: #38bdf8; }

/* Chat input */
.stChatInput input {
    background-color: #020617 !important;
    border-radius: 999px !important;
    border: 1px solid #4b5563 !important;
    color: #e5e7eb !important;
}

.stChatInput input::placeholder {
    color: #6b7280 !important;
}

.stChatInput > div {
    padding-top: 0.4rem;
}

/* Hide default Streamlit header/footer */
header[data-testid="stHeader"] {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.markdown(
    '<h1 class="toji-title">Toji • Groq Q&A Chatbot</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="toji-subtitle">Ask anything and let <b>Toji</b> reason with Groq-powered Llama 3.1.</p>',
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "conversation" not in st.session_state:
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant",
        temperature=0.4,
    )
    memory = ConversationBufferMemory()
    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False,
    )

with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            with st.chat_message("user", avatar="🧑"):
                st.markdown(
                    f"""
                    <div class="toji-message toji-user">
                        <div class="msg-header msg-user-name">You</div>
                        <div>{msg["content"]}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            with st.chat_message("assistant", avatar="⚡"):
                st.markdown(
                    f"""
                    <div class="toji-message toji-bot">
                        <div class="msg-header msg-bot-name">Toji</div>
                        <div>{msg["content"]}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    st.markdown("</div>", unsafe_allow_html=True)

user_input = st.chat_input("Type your message for Toji...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user", avatar="🧑"):
        st.markdown(
            f"""
            <div class="toji-message toji-user">
                <div class="msg-header msg-user-name">You</div>
                <div>{user_input}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    response = st.session_state.conversation.predict(input=user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant", avatar="⚡"):
        st.markdown(
            f"""
            <div class="toji-message toji-bot">
                <div class="msg-header msg-bot-name">Toji</div>
                <div>{response}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
