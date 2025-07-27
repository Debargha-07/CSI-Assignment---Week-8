
from retriever import retrieve_top_docs
from generator import generate_answer, is_scribble_or_nonsense
from utils import load_data  # REQUIRED to get full DataFrame

# Load full DataFrame once
df = load_data("data/training.csv")

print("\n🤖 Welcome to the Loan Document Q&A Chatbot!")
print("Ask me anything about loan applicants, income, approvals, etc.\nType 'exit' to quit.\n")

while True:
    user_input = input("🧑 You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("\n👋 Goodbye!")
        break

    if is_scribble_or_nonsense(user_input):
        print("🤖 Chatbot: That doesn't look like a valid question. Can you rephrase?")
        continue

    
    docs, _ = retrieve_top_docs(user_input)

    # Use logic-based generator on full dataframe
    response = generate_answer(user_input, df)
    print(f"🤖 Chatbot: {response}")
