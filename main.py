import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_javascript import st_javascript

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=GEMINI_API_KEY
)

# Simulate workflow automation
def simulate_workflow(task):
    st.success(f"✅ {task}")

# Classify and simulate based on query
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

# Streamlit UI
st.set_page_config(page_title="AI Customer Support Agent", layout="centered")
st.title("💬 AI Customer Support Agent")
st.markdown("""
Welcome to your **smart AI support assistant**. You can ask questions, book appointments,
send emails, or handle customer service tasks using your **voice or text**.
Powered by **Gemini AI** for intelligent and automated support.
""")
add_vertical_space(1)

# Input Mode
input_mode = st.radio("Choose Input Mode:", ["📝 Text Input", "🎤 Voice Input"])
user_query = ""

# Input Handler
if input_mode == "📝 Text Input":
    user_query = st.text_input("Type your request:")
else:
    st.info("Click the mic icon and speak...")
    result = st_javascript("""
        const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

        async function recordVoice() {
          const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
          recognition.lang = 'en-US';
          recognition.interimResults = false;
          recognition.maxAlternatives = 1;

          return await new Promise((resolve, reject) => {
            recognition.onresult = (event) => {
              const text = event.results[0][0].transcript;
              resolve(text);
            };
            recognition.onerror = (event) => {
              reject("Error: " + event.error);
            };
            recognition.start();
          });
        }

        await sleep(100);
        try {
            const result = await recordVoice();
            return result;
        } catch (e) {
            return e;
        }
    """)
    if result:
        user_query = result
        st.success(f"You said: {result}")

# AI + Task Execution
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
