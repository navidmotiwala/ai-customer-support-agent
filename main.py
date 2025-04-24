import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_javascript import st_javascript

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=GEMINI_API_KEY
)

# Simulate a support workflow
def simulate_workflow(task):
    st.success(f"✅ {task}")

# Classify query and simulate task
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

# Input mode
input_mode = st.radio("Choose Input Mode:", ["📝 Text Input", "🎤 Voice Input"])
user_query = ""

if input_mode == "📝 Text Input":
    user_query = st.text_input("Type your request:")

else:
    st.markdown("### 🎙️ Click the button below to start speaking")
    if st.button("🎤 Start Voice Recording"):
        st.info("🎙️ Listening... Please speak into your mic.")
        result = st_javascript("""
            const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

            async function recordVoice() {
              try {
                await navigator.mediaDevices.getUserMedia({ audio: true }); // 🔐 Ask for mic access
              } catch (err) {
                return "❌ Mic permission denied";
              }

              const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
              recognition.lang = 'en-US';
              recognition.interimResults = false;
              recognition.maxAlternatives = 1;

              return await new Promise((resolve, reject) => {
                recognition.onresult = (event) => {
                  const text = event.results[0][0].transcript;
                  resolve(text);
                };
                recognition.onspeechend = () => {
                  recognition.stop();
                };
                recognition.onerror = (event) => {
                  reject("❌ Speech error: " + event.error);
                };
                recognition.start();
              });
            }

            await sleep(200);
            try {
                const result = await recordVoice();
                return result;
            } catch (e) {
                return e;
            }
        """)

        if result and not result.startswith("❌"):
            user_query = result
            st.success(f"You said: {result}")
        else:
            st.warning(result if result else "🎤 Didn't catch anything. Try again and allow mic access.")

# Process input
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
