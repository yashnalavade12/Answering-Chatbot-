import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd

# Load dataset
df = pd.read_csv("chatbot_dataset.csv")

# Convert to dictionary for easy lookup
qa_pairs = dict(zip(df['User Query'], df['Bot Response']))

def chatbot():
    print(" Chatbot is ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ").lower().strip()
        if user_input == "exit":
            print("Bot: Goodbye!")
            break
        # Check if query exists
        if user_input in qa_pairs:
            print("Bot:", qa_pairs[user_input])
        else:
            print("Bot: Sorry, I don’t know that yet. Please rephrase or add it to my dataset!")

chatbot()
