# AI Study Assistant Chatbot

## Project Title
AI Question-Answering Chatbot

## Objective
Build a simple chatbot using LangChain that accepts a question from the user and generates an AI answer.

## Topic
Study Assistant

## Technologies Used
- Python
- LangChain
- Gemini
- Python Dotenv

## Features
- Accepts questions from the user
- Generates AI answers
- Uses a prompt template
- Uses Gemini as the language model
- Stores the API key in a .env file
- Includes basic error handling

## Testing
The chatbot was tested with five questions:
1. What is Artificial Intelligence?
2. What is Machine Learning?
3. What is Deep Learning?
4. What is Python?
5. What is a neural network?

## API Key Setup
Create a `.env` file in the project folder and add:
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
Replace `YOUR_GEMINI_API_KEY` with your own Gemini API key.
Do not upload the `.env` file to GitHub.

## Project Files
- app.py
- requirements.txt
- README.md
- .gitignore

Note: The `.env` file is kept locally and is not uploaded to GitHub because it contains the Gemini API key.
