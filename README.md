# Answering-Chatbot-
🤖 Basic Chatbot using Python and CSV

A simple rule-based chatbot built with Python and Pandas.
It uses a CSV file (chatbot_dataset.csv) that stores predefined queries and responses, making it easy to extend and customize.

📌 Features

Reads Q&A pairs from a CSV file

Handles greetings, FAQs, and study-related queries

Beginner-friendly, simple Python code

Easily expandable — just add more queries in the CSV

🚀 How It Works

The chatbot loads chatbot_dataset.csv using Pandas.

It maps each User Query → Bot Response.

The user types input in the terminal.

If input matches a query, the bot replies with the response.

If not found, the bot returns a fallback message.

🛠️ Tech Stack

Python 3.13+

Pandas (for reading CSV)

CSV file (knowledge base)

📂 Project Structure
📁 chatbot-project
│── chatbot_dataset.csv   # Dataset with queries & responses
│── chatboot.py           # Main chatbot script
│── README.md             # Project documentation

▶️ Usage

Clone this repo:

git clone https://github.com/your-username/chatbot-project.git
cd chatbot-project


Install requirements:

pip install pandas


Run the chatbot:

python chatboot.py

💡 Example Interaction
Chatbot is ready! Type 'exit' to quit.
You: hello
Bot: Hi! How can I help you today?

You: what can you do
Bot: I can answer questions, explain chapters, and help you study effectively.

You: bye
Bot: Goodbye! Have a great day!

🔮 Future Improvements

Add fuzzy matching (so queries don’t need exact wording).

Integrate NLP models for smarter answers.

Use PDF knowledge extraction as chatbot memory.
