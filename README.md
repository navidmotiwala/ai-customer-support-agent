# AI Customer Support Agent

## Description

Welcome to **AI Customer Support Agent**! This project leverages **Gemini AI** to provide automated customer support. The agent can handle various customer service tasks such as booking appointments, sending greeting emails, providing answers to general queries, updating order statuses, handling issues, and much more. The system is designed to accept both **text input** and **voice input**, making it interactive and user-friendly.

## Features

- **Voice Input**: Speak to the AI assistant and it will process your requests using speech recognition.
- **Text Input**: Type your query and receive responses from Gemini AI.
- **Automated Support Tasks**: The AI will classify your request and simulate various support tasks like booking an appointment, sending emails, handling orders, and more.
- **Gemini AI Integration**: Powered by Gemini AI for intelligent query processing and support task automation.

## Installation

To run this application locally, follow these steps:

### Prerequisites

Ensure you have Python 3.7+ installed on your machine.

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/ai-customer-support-agent.git
    ```

2. Navigate to the project directory:
    ```bash
    cd ai-customer-support-agent
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - **Mac/Linux**:
      ```bash
      source venv/bin/activate
      ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Setting Up Environment Variables

1. Create a `.env` file in the project directory.
2. Add your **Gemini API Key** to the `.env` file:
    ```plaintext
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

## Running the Application

1. Run the app:
    ```bash
    streamlit run app.py
    ```

2. The application should now be running locally. Open your browser and navigate to `http://localhost:8501` to start interacting with your AI customer support agent.

## Usage

1. Once the app is running, you will be prompted to choose between **text input** or **voice input**.
2. Type or speak your query, and the AI will respond with an appropriate action.
3. The agent can handle tasks like:
   - Booking appointments 📅
   - Sending greeting emails 📧
   - Answering customer questions 💡
   - Updating order statuses 📦
   - Handling issues 🛠️
   - And more!

## Example Queries

Here are some example queries to try:

### Appointment Booking:
- "I want to book an appointment for tomorrow at 3 PM."
- "Can you please book an appointment for a consultation?"

### Sending Emails:
- "Send a greeting email to my friend."
- "Can you send an email that says 'Welcome to our service!'?"

### General Queries:
- "I have a question about your services."
- "Can you help me with my order?"

### Order/Status Queries:
- "I want to order a pizza."
- "I just placed an order, can I check its status?"

### Problem Handling:
- "There's a problem with my last order."
- "I'm facing an issue with the app."

## Contributing

If you'd like to contribute to the project, please fork the repository and submit a pull request. Make sure to follow the coding standards and write tests for new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Muhammad | [Email](mailto:muhammadzohaib1415@gmail.com) 
