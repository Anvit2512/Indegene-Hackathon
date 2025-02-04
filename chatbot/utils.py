import openai
import os
from dotenv import load_dotenv


# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_emotional_support(user_input):
    """Generates an empathetic response to user input."""
    prompt = f"""
    You are a compassionate mental health AI assistant. A user is seeking emotional support.
    
    User: "{user_input}"
    
    Provide a thoughtful, empathetic, and supportive response. Keep it warm and encouraging, avoiding clinical or robotic language.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a kind and supportive AI mental health assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.8,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"I'm sorry, an error occurred: {e}"
