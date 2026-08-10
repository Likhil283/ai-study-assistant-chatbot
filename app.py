import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load API key
load_dotenv()

# Connect Gemini
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Create prompt
prompt = ChatPromptTemplate.from_template(
    """You are a helpful Study Assistant.
Answer the student's question clearly and simply.

Question: {question}"""
)

# Create LangChain chain
chain = prompt | model

# Start chatbot
print("AI Study Assistant")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chatbot stopped.")
        break

    try:
        response = chain.invoke({"question": question})

        if isinstance(response.content, list):
            answer = response.content[0]["text"]
        else:
            answer = response.content

        print("AI:", answer)

    except Exception as e:
        print("Error:", e)
