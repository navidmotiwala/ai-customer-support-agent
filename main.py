import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import speech_recognition as sr
from streamlit_extras.add_vertical_space import add_vertical_space

# Load environment variables
load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=GEMINI_API_KEY
)

# Function to simulate automation task
def simulate_workflow(task):
    st.success(f"✅ {task}")

# Voice Input Handler
def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        st.success(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        st.error("Sorry, could not understand audio.")
    except sr.RequestError:
        st.error("Could not request results. Check internet connection.")
    return ""

# Advanced customer support workflow classification
def classify_and_simulate(query):
    lowered = query.lower()
    if "book" in lowered and "appointment" in lowered:
        simulate_workflow("📅 Appointment booked. A confirmation email has been sent.")
    elif "send" in lowered and "email" in lowered:
        simulate_workflow("📧 Greeting email has been sent to the recipient.")
    elif "question" in lowered or "help" in lowered or "support" in lowered:
        simulate_workflow("💡 Answer provided to the customer's query.")
    elif "status" in lowered:
        simulate_workflow("📦 Order/status has been updated and the customer notified.")
    elif "order" in lowered or "food" in lowered:
        simulate_workflow("🍔 Order logged and sent to the kitchen.")
    elif "problem" in lowered or "issue" in lowered:
        simulate_workflow("🛠️ Issue recorded. A support agent will follow up.")
    else:
        simulate_workflow("📝 CRM entry created. A support follow-up is scheduled.")

# UI Setup
st.set_page_config(page_title="AI Customer Support Agent", layout="centered")
st.title("💬 AI Customer Support Agent")
st.markdown("""
Welcome to your **smart AI support assistant**. You can ask questions, book appointments,
send emails, or handle customer service tasks using your **voice or text**.
Powered by **Gemini AI** for intelligent and automated support.
""")

add_vertical_space(1)

# User selects input mode
input_mode = st.radio("Choose Input Mode:", ["📝 Text Input", "🎤 Voice Input"])

# Get user query
if input_mode == "📝 Text Input":
    user_query = st.text_input("Type your request:")
else:
    if st.button("🎙️ Start Recording"):
        user_query = get_voice_input()
    else:
        user_query = ""

# Handle response
if user_query:
    st.markdown("---")
    st.subheader("🤖 Gemini's Response")
    response = llm.invoke(user_query)
    st.success(response.content)

    st.markdown("---")
    st.subheader("🔧 Support Task Execution")
    classify_and_simulate(user_query)

    st.balloons()

st.markdown("---")
st.caption("Made with ❤️ by Muhammad | Powered by Gemini ✨")
