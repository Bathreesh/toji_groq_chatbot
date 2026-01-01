# GROQ ChatBot Project

A **GROQ-powered** AI chatbot built with Python and Streamlit that provides low-latency conversational responses through a clean web interface. The chatbot connects to Groq’s language models via the Groq API to deliver fast and efficient inference for everyday question-answering and experimentation.

---

## 🚀 Live Demo

Try the deployed application here:

👉 **Streamlit App:** https://tojigroqchatbot-buhmrwrxpkdfzevrbtolde.streamlit.app/

---

## 💡 Key Features

- Chat-style web interface built with Streamlit for intuitive interaction.  
- Integration with Groq API for high-speed LLM responses and reduced latency.  
- Session-based conversation history to maintain context across multiple prompts.  
- Simple, extensible codebase (main `app.py` plus `requirements.txt`) for easy customization and learning.

---

## 🧱 Tech Stack

- **Language:** Python 3.10+  
- **Framework:** Streamlit  
- **LLM Provider:** Groq API (configurable model name in code)  
- **Deployment:** Streamlit Community Cloud

---

## 📦 Project Structure

- `app.py`: Contains the Streamlit UI, session state management, and calls to the Groq API for generating responses.  
- `requirements.txt`: Lists all libraries required to run the project, including Streamlit and Groq client dependencies.

---

## ⚙️ Installation

Follow these steps to run the project locally.

1. **Clone the repository**


2. **(Optional) Create and activate a virtual environment**


3. **Install dependencies**


4. **Configure environment variables**

Obtain your API key from the Groq Console and set it as an environment variable (for example `GROQ_API_KEY`):


If you prefer, you can store secrets in a `.env` file or in Streamlit’s `secrets.toml`.

5. **Run the Streamlit app**


This will start a local server, typically at `http://localhost:8501`. Open the URL in your browser to access the chatbot.

---

## 💬 How to Use

- Open the app (locally or via the live demo link).  
- Type your question or prompt into the input area of the chat interface.  
- Submit the prompt to receive a response from the selected Groq model.  
- Continue the conversation by asking follow-up questions; the app maintains context within the session.

---

## 🔧 Configuration & Customization

You can adapt the chatbot to your needs:

- **Model selection:** Update the model name or parameters in `app.py` to switch between available Groq models.  
- **System prompt / persona:** Modify the initial system message to control tone, role, or domain focus (e.g., coding assistant, study helper, support bot).  
- **UI changes:** Customize layout, theme, and additional controls (temperature, max tokens, model selector, etc.) using Streamlit widgets.

---

## 🌐 Deployment

This project is ready for deployment on Streamlit Community Cloud:

1. Push your code to GitHub (`Bathreesh/GROQ_ChatBot_Project`).  
2. In Streamlit Community Cloud, create a new app from this repository.  
3. Configure environment variables such as `GROQ_API_KEY` in the app’s “Secrets” or environment settings.  
4. Deploy and share the generated URL (for example, the live demo link above).

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.  
2. Create a new branch for your feature or bugfix.  
3. Commit your changes with clear, descriptive messages.  
4. Open a pull request explaining what you changed and why.

Good practices such as clear code structure, type hints, and concise documentation are appreciated.



